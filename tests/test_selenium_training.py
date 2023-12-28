from selenium import webdriver
from utilities.config_reader import data, browsers_config, headless_mode_config
from pages.selenium_training_page import SeleniumTrainingPage
from utilities.exception_logger import log_exception

class TestSeleniumTrainingPage():
    _selenium_training_page = None
    _DRIVER = None
    _OPTIONS = None

    def __init__(self, browser, URL, headless_mode):        
        if(browser == 'Firefox'):
            self._OPTIONS = webdriver.FirefoxOptions().add_argument('--headless=new') if headless_mode else None
            self._DRIVER = webdriver.Firefox(options=self._OPTIONS)                        
        elif(browser == 'Edge'):
            self._OPTIONS = webdriver.EdgeOptions().add_argument('--headless=new') if headless_mode else None
            self._DRIVER = webdriver.Edge(options=self._OPTIONS)

        self._selenium_training_page = SeleniumTrainingPage(self._DRIVER, URL)

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


# ==========================  Init tests  =====================================

MAIN_PAGE_URL = data['pages']['selenium_training_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    selenium_training_page = TestSeleniumTrainingPage(browser, MAIN_PAGE_URL, HEADLESS_MODE)

    try:
        selenium_training_page.click_faqs() \
                               .extract_enrolled_count() \
                               .extract_what_is_included()
    except Exception as ex:
        log_exception(ex, HEADLESS_MODE, selenium_training_page, 'selenium_training_page')
     
    selenium_training_page.__exit__()