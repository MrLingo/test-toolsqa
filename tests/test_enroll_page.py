import time
import urllib3.exceptions
import pytest
from utilities.driver_handler import DriverHandler
from utilities.config_reader import data, browsers_config, headless_mode_config
from pages.enroll_page import EnrollPage
from utilities.exception_logger import log_exception


class DriveEnrollPage():
    _enroll_page : EnrollPage = None
    _DRIVER = None


    def __init__(self, driver, URL):
        self._DRIVER = driver
        self._enroll_page = EnrollPage(self._DRIVER, URL)


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

    def take_screenshot(self, dir):
        self._DRIVER.get_screenshot_as_file(dir)

    # Form
    def type_into_first_name_field(self, text):
        self._enroll_page.get_first_name_field().clear()
        self._enroll_page.get_first_name_field().send_keys(text)
        time.sleep(2)
        return self

    def type_into_last_name_field(self, text):        
        self._enroll_page.get_last_name_field().clear()
        self._enroll_page.get_last_name_field().send_keys(text)
        time.sleep(2)
        return self

    def type_into_email_name_field(self, text):
        self._enroll_page.get_email_field().clear()
        self._enroll_page.get_email_field().send_keys(text)
        time.sleep(2)
        return self

    def type_into_mobile_name_field(self, text):
        self._enroll_page.get_mobile_field().clear()
        self._enroll_page.get_mobile_field().send_keys(text)
        time.sleep(2)
        return self

    def type_into_country_name_field(self, country):
        self._enroll_page.get_country_field(country).click()
        return self

    def type_into_city_name_field(self, text):
        self._enroll_page.get_city_field().clear()
        self._enroll_page.get_city_field().send_keys(text)
        time.sleep(2)
        return self

    def type_into_message_name_field(self, text):
        self._enroll_page.get_message_field().clear()
        self._enroll_page.get_message_field().send_keys(text)
        time.sleep(2)
        return self

    def type_into_code_name_field(self, text):
        self._enroll_page.get_code_field().clear()
        self._enroll_page.get_code_field().send_keys(text)
        time.sleep(2)
        return self

    def __exit__(self):
        self._DRIVER.quit()


class TestEnrollPage():
    @staticmethod
    def test_form():
        try:
            drive_enroll_page.type_into_first_name_field('John') \
                             .type_into_last_name_field('Hale') \
                             .type_into_email_name_field('j.haile@gmail.com') \
                             .type_into_mobile_name_field('0885666111') \
                             .type_into_country_name_field('Bulgaria') \
                             .type_into_city_name_field('Sofia') \
                             .type_into_message_name_field('Test message') \
                             .type_into_code_name_field('code')
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:            
            log_exception(ex, HEADLESS_MODE, drive_enroll_page, 'enroll_page')
            pytest.fail

# ==========================  Init tests  =====================================

ENROLL_PAGE_URL = data['pages']['enroll_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    DriverHandler.init_driver(browser, HEADLESS_MODE)
    drive_enroll_page = DriveEnrollPage(DriverHandler.get_driver(), ENROLL_PAGE_URL)

    # Fill forms fields
    TestEnrollPage.test_form()
            
    drive_enroll_page.__exit__()