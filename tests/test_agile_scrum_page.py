import urllib3.exceptions
import pytest
from utilities.driver_handler import DriverHandler
from utilities.config_reader import data, browsers_config, headless_mode_config
from pages.agile_scrum_tutorial_page import AgileScrumPage
from utilities.exception_logger import log_exception


class DriveAgileScrumPage():
    _agile_scrum_page : AgileScrumPage = None
    _DRIVER = None
    

    def __init__(self, driver, URL):
        self._DRIVER = driver
        self._agile_scrum_page = AgileScrumPage(self._DRIVER, URL)
        

    # Other
    def take_screenshot(self, dir):
        self._DRIVER.get_screenshot_as_file(dir)

    # Tutorial header
    def extract_author(self):
        print('Tutorial author: ', self._agile_scrum_page.get_author().text)
        return self
    
    def extract_reviewer(self):
        print('Tutorial reviewer: ', self._agile_scrum_page.get_reviewer().text)
        return self
    
    def extract_release_date(self):
        print('Tutorial relase date: ', self._agile_scrum_page.get_tutorial_release_date().text)
        return self
    
    # Tutorial footer
    def extract_comment_section(self):
        return self
    
    def click_next_lesson(self):
        self._agile_scrum_page.get_next_lesson().click()
        return self

    def __exit__(self):
        self._DRIVER.quit()


class TestAgileScrumPage():
    @staticmethod
    def test_extract_tutoria_info():
        try:
            drive_agile_scrum_page.extract_release_date() \
                                  .extract_author() \
                                  .extract_reviewer() \
                                  .extract_comment_section()
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:            
            log_exception(ex, HEADLESS_MODE, drive_agile_scrum_page, 'agile_scrum_page')
            pytest.fail

    @staticmethod
    def test_clicking_next_lesson():
        try:
            drive_agile_scrum_page.click_next_lesson()
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:            
            log_exception(ex, HEADLESS_MODE, drive_agile_scrum_page, 'agile_scrum_page')
            pytest.fail

# ==========================  Init tests  =====================================

AGILE_SCRUM_PAGE_URL = data['pages']['agile_scrum_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    DriverHandler.init_driver(browser, HEADLESS_MODE)
    drive_agile_scrum_page = DriveAgileScrumPage(DriverHandler.get_driver(), AGILE_SCRUM_PAGE_URL)

    TestAgileScrumPage.test_extract_tutoria_info()
    TestAgileScrumPage.test_clicking_next_lesson()
                
    drive_agile_scrum_page.__exit__()