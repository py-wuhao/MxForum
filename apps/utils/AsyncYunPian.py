import json
from urllib.parse import urlencode
from functools import partial

import tornado
from tornado.httpclient import AsyncHTTPClient, HTTPRequest


class AsyncYunPian:
    def __init__(self, api_key):
        self.api_key = api_key

    async def send_single_sms(self, code, mobile):
        url = "https://sms.yunpian.com/v2/sms/single_send.json"
        text = "【wh吴昊】您的验证码是{}".format(code)
        body = urlencode({
            'apikey': self.api_key,
            'mobile': mobile,
            'text': text
        })
        http_client = AsyncHTTPClient()
        request = HTTPRequest(url, method='POST', body=body)
        # try:
        #     response = await http_client.fetch(request)
        # except Exception as e:
        #     print('Error: %s' % e)
        # else:
        #     print(json.loads(response.body.decode('utf8')))
        await tornado.gen.sleep(2)
        return {"code": 0,
                "msg": "发送成功",
                "count": 1,
                "fee": 0.05,
                "unit": "RMB",
                "mobile": mobile,
                "sid": 3310228982}


if __name__ == '__main__':
    io_loop = tornado.ioloop.IOLoop.current()
    yun_pian = AsyncYunPian("40f21a82967289fb5b4b3be1ed640ab0")
    send_sms = partial(yun_pian.send_single_sms, '0000', '17762392194')
    io_loop.run_sync(send_sms)
