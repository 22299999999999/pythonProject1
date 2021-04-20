import pytest
import yaml
from selenium import webdriver


def test_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")


def test_print():
    for i in range(1, 3):
        print(i)


def get_yaml():
    with open('./interface/page/contact.yaml', encoding='utf-8') as f:
        print(f)
        print(type(f))

        data = yaml.safe_load(f)
    return data


def test_get_yaml():
    data = get_yaml()
    print(data)
    print(type(data))


def func(x):
    return x + 1


def test_func():
    pytest.assume(func(3) == 5)
    pytest.assume(func(4) == 5)
    print("hello")
