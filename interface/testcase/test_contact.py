import pytest
from interface.page.contact import Contact


class TestContact():

    def setup(self):
        self.cont = Contact()
        # self.phone = self.cont.phone_num

    def test_get_token(self):
        r = self.cont.get_token()
        assert 0 == r.get('errcode')

    @pytest.mark.parametrize("userid,name,mobile,department,alias",
                             [('159374513', '接口添加', '13567898907', [1], 'jackzhang')])
    def test_add_member(self, userid, name, mobile, department, alias):
        member = self.cont.find_member(userid)
        if member.get('userid') is not None:
            self.cont.delete_member(userid)
        r = self.cont.add_member(userid=userid, name=name, mobile=mobile, department=department, alias=alias)
        try:
            final_name = self.cont.find_member(userid)
        finally:
            self.cont.delete_member(userid)
        assert name == final_name['name']

    @pytest.mark.parametrize("userid", range(20))
    def test_find_member(self, userid):
        member = self.cont.find_member(userid)
        if member.get('userid') is None:
            self.cont.add_member(userid=userid, name="1", mobile=self.cont.phone_num(), department=[1], alias="昵称")
        r = self.cont.find_member(userid=userid)
        assert 0 == r.get('errcode')

    @pytest.mark.parametrize("userid,name", [('name13', '接口修改')])
    def test_update_member(self, userid, name):
        member = self.cont.find_member(userid)
        if member.get('userid') is None:
            self.cont.add_member(userid=userid, name="1", mobile=self.cont.phone_num, department=[1], alias="昵称")
        r = self.cont.update_member(userid=userid, name=name)
        assert 0 == r.get('errcode')

    @pytest.mark.parametrize("userid", [('333111')])
    def test_delete_member(self, userid):
        member = self.cont.find_member(userid)
        if member.get('userid') is None:
            self.cont.add_member(userid=userid, name="1", mobile=self.cont.phone_num(), department=[1], alias="昵称")
        r = self.cont.delete_member(userid=userid)
        assert 0 == r.get('errcode')
