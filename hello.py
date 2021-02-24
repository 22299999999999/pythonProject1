from selenium import webdriver


def test_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")


def test_print():
    for i in range(1, 3):
        print(i)
