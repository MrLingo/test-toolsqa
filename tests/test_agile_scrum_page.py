import time
import json

from selenium import webdriver
from pages.agile_scrum_tutorial_page import AgileScrumPage

class TestAgileScrumPage():
    _articles_page = None
    _DRIVER = None
    _OPTIONS = None

    def __init__(self, browser, URL, headless_mode):        
        if(browser == 'Firefox'):
            self._OPTIONS = webdriver.FirefoxOptions().add_argument('--headless=new') if headless_mode else None
            self._DRIVER = webdriver.Firefox(options=self._OPTIONS)                        
        elif(browser == 'Edge'):
            self._OPTIONS = webdriver.EdgeOptions().add_argument('--headless=new') if headless_mode else None
            self._DRIVER = webdriver.Edge(options=self._OPTIONS)

        self._articles_page = AgileScrumPage(self._DRIVER, URL)

    # Other
    def go_to_original_tab(self, curr_window_handle):        
        handles = self._DRIVER.window_handles

        for window in handles:
            if window != curr_window_handle:
                self._DRIVER.switch_to.window(curr_window_handle)
                return self
            
    def go_back(self):
        self._DRIVER.back()
        return self

    def get_current_window(self):
        return self._DRIVER.current_window_handle

    def close_current_window(self):
        self._DRIVER.close()
    
    # Tutorial header
    def extract_author(self):
        print('Tutorial author: ', self._articles_page.get_author().text)
        return self
    
    def extract_reviewer(self):
        print('Tutorial reviewer: ', self._articles_page.get_reviewer().text)
        return self
    
    def extract_release_date(self):
        print('Tutorial relase date: ', self._articles_page.get_tutorial_release_date().text)
        return self
    
    # Tutorial footer
    def extract_comment_section(self):
        return self
    
    def click_next_lesson(self):
        self._articles_page.get_next_lesson().click()
        return self

    def __exit__(self):
        self._DRIVER.quit()


# ==========================  Init tests  =====================================

# Read configuration
config_file = open('config/config.json')
data = json.load(config_file)
config_file.close()

MAIN_PAGE_URL = data['pages']['agile_scrum_page']
BROWSERS = [browser for browser in data['browsers']]
HEADLESS_MODE = data['headless_mode']

# Test on all browsers
for browser in BROWSERS:
    _agile_scrum_page = TestAgileScrumPage(browser, MAIN_PAGE_URL, HEADLESS_MODE)

    _agile_scrum_page.extract_release_date() \
                     .extract_author() \
                     .extract_reviewer() \
                     .extract_comment_section() \
                     .click_next_lesson()
        
    _agile_scrum_page.__exit__()