import json

import allure
import pytest
import yaml

from interface.page.contact import Contact


class TestContact():

    def setup(self):
        self.cont = Contact()
        # self.phone = self.cont.phone_num

    @allure.feature("生成token")
    def test_get_token(self):
        r = self.cont.get_token()
        assert 0 == r.get('errcode')

    @allure.feature("添加成员")
    # @pytest.mark.parametrize("userid,name,mobile,department,alias",
    #                          [('159374513', '接口添加', '13567898907', [1], 'jackzhang')])
    @pytest.mark.parametrize("userid,name,mobile,department,alias",
                             yaml.safe_load(open("./../page/contact.yaml", encoding="utf-8")))
    def test_add_member(self, userid, name, mobile, department, alias):
        with allure.step("查询成员"):
            member = self.cont.find_member(userid)
        with allure.step("成员是否存在"):
            if member.get('userid') is not None:
                with allure.step("成员存在，删除成员"):
                    self.cont.delete_member(userid)
        with allure.step("调用成员添加接口"):
            r = self.cont.add_member(userid=userid, name=name, mobile=mobile, department=department, alias=alias)
        try:

            final_name = self.cont.find_member(userid)
            print(final_name)

        finally:
            self.cont.delete_member(userid)
        with allure.step("断言是否添加成功"):
            assert str(userid) == final_name['userid']

    # 结合python的pytest-xdist第三方包，实现并行运行。运行时添加-n auto参数
    @pytest.mark.parametrize("userid", range(20))
    def test_find_member(self, userid):
        member = self.cont.find_member(userid)
        if member.get('userid') is None:
            self.cont.add_member(userid=userid, name="1", mobile=self.cont.phone_num(), department=[1], alias="昵称")
        r = self.cont.find_member(userid=userid)
        assert 0 == r.get('errcode')

    @pytest.mark.parametrize('userid,name', [('ZhengZhenZhen', '接口修改')])
    def test_update_member(self, userid, name):
        r = self.cont.update_member(userid=userid, name=name)
        assert 0 == r.get('errcode')

    @pytest.mark.parametrize("userid", [('333111')])
    def test_delete_member(self, userid):
        member = self.cont.find_member(userid)
        if member.get('userid') is None:
            self.cont.add_member(userid=userid, name="1", mobile=self.cont.phone_num(), department=[1], alias="昵称")
        r = self.cont.delete_member(userid=userid)
        assert 0 == r.get('errcode')

    def test_data(self):
        print(yaml.safe_load(open("./../page/contact.yaml", encoding="utf-8")))
