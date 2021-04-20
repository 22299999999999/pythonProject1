import random
import string

import requests
import yaml
from requests import Session


class BasePage():

    def __init__(self):
        self.s = Session()
        self.corpid = "ww3163f14b4cb2695e"
        self.corpsecret = "C7DyoQdw3BHkIUL7qZeQomxDupfKhMul-LJSy6fJGEY"
        self.s.params["access_token"] = self.get_token().get('access_token')

    def get_token(self, corpid=None, corpsecret=None):
        if corpid is None:
            corpid = self.corpid
        if corpsecret is None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=params)
        print(r.json())
        return r.json()

    def phone_num(self):
        all_phone_nums = set()
        num_start = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '158', '159', '157', '182', '187',
                     '188',
                     '147', '130', '131', '132', '155', '156', '185', '186', '133', '153', '180', '189']

        start = random.choice(num_start)
        end = ''.join(random.sample(string.digits, 8))
        res = start + end
        return res

    def get_yaml(self):
        with open('../page/contact.yaml', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
