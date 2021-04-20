import pytest


@pytest.fixture(scope='module', autouse=True)
def login():
    print("登录前")
    yield
    print("退出")


class TestDemo():
    def test_add(self):
        print("add")

    def test_add2(self):
        print("add2")


class TestDemo2():
    def test_add3(self):
        print("add3")

    def test_add4(self):
        print("add4")
