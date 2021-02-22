import pytest
from selenium import webdriver
import time


class TestHog:
    def setup_method(self):
        self.driver = webdriver.Chrome()

        # 隐式等待  最多等待5s，等待过程中动态结束等待
        self.driver.implicitly_wait(5)
        print("setup")

    def teardown_method(self):
        self.driver.quit()
        print("teardowm")

    @pytest.mark.skip
    def test_hog(self):
        self.driver.get("https://baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")

        element.click()
        time.sleep(5)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(10)

    def test_12306(self):
        self.driver.get("https://www.12306.cn/index/")
        element2 = self.driver.execute_script("a=document.getElementById('train_date'),a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(10)
