import pytest


@pytest.fixture(scope='session', autouse=True)
def login():
    print("conftest登录")
    yield
    print("conftest退出")
