import string
import random
from typing import List
import requests

from interface.page.base_page import BasePage


class Contact(BasePage):

    def add_member(self, userid: str, name: str, mobile: str, department: List[int], **kwargs):
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        r = self.s.post(url=url, json=data)
        return r.json()

    def find_member(self, userid):
        params = {"userid": userid}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        r = self.s.get(url=url, params=params)
        return r.json()

    def update_member(self, userid: str, **kwargs):
        data = {
            "userid": userid,
        }
        data.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/update'
        r = self.s.post(url=url, json=data)
        return r.json()

    def delete_member(self, userid: str):
        params = {"userid": userid}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/delete'
        r = self.s.post(url=url, params=params)
        return r.json()
