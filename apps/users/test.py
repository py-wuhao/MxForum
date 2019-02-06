import json

import requests

web_url = 'http://127.0.0.1:8888'


def test_sms():
    url = '{}/code/'.format(web_url)
    data = {
        'mobile': '17762392194'
    }
    res = requests.post(url, json=data)
    print(json.loads(res.text))


def test_register():
    url = '{}/register/'.format(web_url)
    data = {
        'mobile': '17762392194',
        'code': '8203',
        'password': 'abcdefg'
    }
    res = requests.post(url, json=data)
    print(json.loads(res.text))


if __name__ == '__main__':
    # test_sms()
    test_register()
