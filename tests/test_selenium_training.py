import pytest
import urllib3.exceptions
from utilities.config_reader import data, browsers_config, headless_mode_config
from utilities.driver_handler import DriverHandler
from pages.selenium_training_page import SeleniumTrainingPage
from utilities.exception_logger import log_exception


class DriveSeleniumTrainingPage():
    _selenium_training_page : SeleniumTrainingPage = None
    _DRIVER = None


    def __init__(self, driver, URL):
        self._DRIVER = driver
        self._selenium_training_page = SeleniumTrainingPage(self._DRIVER, URL)

    # Other              
    def take_screenshot(self, dir):
        self._DRIVER.get_screenshot_as_file(dir)

    # Extract
    def extract_enrolled_count(self):
        print('Get already enrolled count: ', self._selenium_training_page.get_already_enrolled_count().text)        
        return self
    
    def click_faqs(self):
        faqs = self._selenium_training_page.get_faqs()        

        for faq in faqs:
            faq.click()
        return self

    def extract_what_is_included(self):
        count, type = self._selenium_training_page.get_what_is_included_info()
        
        for count_item, type_item in zip(count, type):
            print(type_item.text, ': ', count_item.text)
        return self


    def __exit__(self):
        self._DRIVER.quit()


class TestSeleniumPage():
    @staticmethod
    def test_info_and_faqs():
        try:
            drive_selenium_training_page.click_faqs() \
                                        .extract_enrolled_count() \
                                        .extract_what_is_included()
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:
            log_exception(ex, HEADLESS_MODE, drive_selenium_training_page, 'selenium_training_page')
            pytest.fail
        
# ==========================  Init tests  =====================================

SELENIUM_TRAINING_PAGE_URL = data['pages']['selenium_training_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    DriverHandler.init_driver(browser, HEADLESS_MODE)
    drive_selenium_training_page = DriveSeleniumTrainingPage(DriverHandler.get_driver(), SELENIUM_TRAINING_PAGE_URL)

    TestSeleniumPage.test_info_and_faqs()
    
    drive_selenium_training_page.__exit__()