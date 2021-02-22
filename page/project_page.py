from time import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.project_detail_page import ProjectDetailPage


class ProjectPage(BasePage):
    def goto_project_detail_page(self):
        self.find(By.CSS_SELECTOR, '.invest-list a:nth-child(1)').click()
        sleep(3)
        return ProjectDetailPage(self.driver)
