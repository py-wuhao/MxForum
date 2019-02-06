from wtforms_tornado import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp

MOBILE_REGEXP = "^1[3578]\d{9}$|^1[48]7\d{8}$|^176\d{8}$"


class SmsCodeForms(Form):
    mobile = StringField(label='手机号码',
                         validators=[DataRequired(message='请输入手机号码'), Regexp(MOBILE_REGEXP, message='请输入有效手机号码', )])


class RegisterForm(Form):
    mobile = StringField(label='手机号码',
                         validators=[DataRequired(message='请输入手机号码'), Regexp(MOBILE_REGEXP, message='请输入有效手机号码', )])
    code = StringField("验证码", validators=[DataRequired(message="请输入验证码")])


class LoginForm(Form):
    mobile = StringField(label='手机号码',
                         validators=[DataRequired(message='请输入手机号码'), Regexp(MOBILE_REGEXP, message='请输入有效手机号码', )])
    password = StringField("密码", validators=[DataRequired(message="请输入密码")])
