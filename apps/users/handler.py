import json
import random
from datetime import datetime

import jwt
from tornado.web import RequestHandler

from .forms import SmsCodeForms, RegisterForm, LoginForm
from ..utils.AsyncYunPian import AsyncYunPian
from .models import User
from MxForum.handler import RedisHandler, BaseHandler


class LoginHandler(BaseHandler):
    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        login_form = LoginForm.from_json(param)  # type:LoginForm
        if login_form.validate():
            mobile = login_form.mobile.data
            password = login_form.password.data

            try:
                user = await self.application.objects.get(User, mobile=mobile)
                if not user.password.check_password(password):
                    self.set_status(400)
                    re_data['non_fields'] = '用户名或密码错误'
                else:
                    payload = {
                        'id': user.id,
                        'nick_name': user.nick_name,
                        'exp': datetime.utcnow()
                    }
                    token = jwt.encode(payload, self.settings['secret_key']).decode()
                    re_data['id'] = user.id
                    if user.nick_name is not None:
                        re_data['nick_name'] = user.nick_name
                    else:
                        re_data['nick_name'] = user.mobile
                    re_data['token'] = token
            except User.DoesNotExist as e:
                self.set_status(400)
                re_data['mobile'] = '用户不存在'
        self.finish(re_data)


class RegisterHandler(RedisHandler):
    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        register_form = RegisterForm.from_json(param)
        if register_form.validate():
            mobile = register_form.mobile.data
            code = register_form.code.data
            password = register_form.password.data

            redis_key = '{}_{}'.format(mobile, code)
            if not self.redis_conn.get(redis_key):
                self.set_status(400)
                re_data['code'] = '验证码错误'
            else:
                try:
                    existed_users = await self.application.objects.get(User, mobile=mobile)
                    self.set_status(400)
                    re_data['mobile'] = '用户已经存在'
                except User.DoesNotExist as e:
                    user = await self.application.objects.create(User, mobile=mobile, password=password)
                    re_data['id'] = user.id
        else:
            self.set_status(400)
            for field, msg in register_form.item():
                re_data[field] = msg[0]
        self.finish(re_data)


class SmsHandler(RedisHandler):
    def generate_code(self):
        code = random.randint(0, 9999)
        return '{:0>4d}'.format(code)

    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        sms_form = SmsCodeForms.from_json(param)
        if sms_form.validate():
            mobile = sms_form.mobile.data
            code = self.generate_code()
            yun_pian = AsyncYunPian("40f21a82967289fb5b4b3be1ed640ab0")
            res = await yun_pian.send_single_sms('0000', '17762392194')
            if res['code'] != 0:
                self.set_status(400)
                re_data['mobile'] = res['msg']
            else:
                # 发送成功 将验证吗写入redis中
                self.redis_conn.set('{}_{}'.format(mobile, code), 1, 60 * 10)
        else:
            self.set_status(400)
            for field, msg in sms_form.errors.items():
                re_data[field] = msg[0]

        self.finish(re_data)
