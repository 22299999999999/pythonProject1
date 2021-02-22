from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.project_page import ProjectPage


class HomePage(BasePage):
    def goto_project_page(self):
        self.scorll()
        sleep(3)
        self.find(By.LINK_TEXT, '我要出借').click()

        return ProjectPage(self.driver)
