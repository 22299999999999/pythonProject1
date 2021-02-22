from selenium.webdriver.common.by import By

from page.base_page import BasePage


class ProjectDetailPage(BasePage):

    def get_project_info(self):
        element = self.find(By.CSS_SELECTOR, '.i-big.i-small-gray')
        print(element.text)
        return element.text
