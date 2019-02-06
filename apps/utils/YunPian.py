import requests


class YunPian:
    def __init__(self, api_key):
        self.api_key = api_key

    def send_single_sms(self, code, mobile):
        # 发送单条短信
        url = "https://sms.yunpian.com/v2/sms/single_send.json"
        text = "【wh吴昊】您的验证码是{}".format(code)
        res = requests.post(url, data={
            "apikey": self.api_key,
            "mobile": mobile,
            "text": text
        })

        return res


if __name__ == "__main__":
    yun_pian = YunPian("40f21a82967289fb5b4b3be1ed640ab0")
    res = yun_pian.send_single_sms("1234", "17762392194")
    print(res.text)
