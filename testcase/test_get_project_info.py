from selenium import webdriver

from page.home_page import HomePage


class TestProject():

    def setup(self):
        self.index_main = HomePage()

    def test_get_project_info(self):
        project_info = self.index_main.goto_project_page().goto_project_detail_page().get_project_info()
        assert "1" in project_info
