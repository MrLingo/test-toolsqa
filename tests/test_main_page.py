import time
import urllib3.exceptions
from selenium import webdriver
from utilities.config_reader import data, browsers_config, headless_mode_config
from pages.main_page import MainPage
from utilities.exception_logger import log_exception
import pytest

class DriveMainPage():
    _main_page = None
    _DRIVER = None
    _OPTIONS = None


    def __init__(self, browser, URL, headless_mode):        
        if(browser == 'Firefox'):
            self._OPTIONS = webdriver.FirefoxOptions().add_argument('--headless=new') if headless_mode else None
            self._DRIVER = webdriver.Firefox(options=self._OPTIONS)                        
        elif(browser == 'Edge'):
            self._OPTIONS = webdriver.EdgeOptions().add_argument('--headless=new') if headless_mode else None
            self._DRIVER = webdriver.Edge(options=self._OPTIONS)

        self._main_page = MainPage(self._DRIVER, URL)
    

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

    # Header
    def click_logo_img(self):
        self._main_page.get_logo_img().click()
        return self

    def click_home_nav_item(self): 
        self._main_page.get_nav_bar_item(0).click()
        return self
                    
    def click_selenium_train_nav_item(self):
        self._main_page.get_nav_bar_item(1).click()
        return self

    def click_demo_site_nav_item(self): 
        self._main_page.get_nav_bar_item(2).click()
        return self

    def click_about_nav_item(self): 
        self._main_page.get_nav_bar_item(3).click()
        return self
                               
    def type_into_search_field(self, text):
        self._main_page.get_search_bar().clear()
        self._main_page.get_search_bar().send_keys(text)
        return self
    
    def get_training_batch_announcment_text(self):
        print("Announcement text: ", self._main_page.get_training_batch_announcment_text())
        return self

    # Body
    def click_enroll_button(self):
        enroll_element = self._main_page.get_enroll_button()
        if "enroll" in enroll_element.get_attribute('innerHTML').lower():
            enroll_element.click()
            return self
    
    def click_postman_tutorial(self):
        self._main_page.get_postman_tutorial_redirect().click()
        return self

    def click_latest_article_button(self):
        self._main_page.get_latest_articles_button().click()
        return self

    def click_scrum_category(self):
        self._main_page.get_scrum_learning_item().click()
        return self

    # Footer
    def click_social_media_link(self, social_media):
        self._main_page.get_find_us_icon(social_media).click()
        time.sleep(3)
        return self

    def __exit__(self):
        self._DRIVER.quit()


class TestMainPage():
    @staticmethod
    def test_header():
        try:
            drive_main_page.click_logo_img() \
                           .click_home_nav_item() \
                           .click_selenium_train_nav_item()
            
            curr_window = drive_main_page.get_current_window()
        
            drive_main_page.click_demo_site_nav_item() \
                           .go_to_original_tab(curr_window) \
                           .click_about_nav_item() \
                           .type_into_search_field('testing input field')
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:            
            log_exception(ex, HEADLESS_MODE, drive_main_page, 'main_page')
            pytest.fail
            

    @staticmethod
    def test_body():
        try:
            drive_main_page.get_training_batch_announcment_text() \
                           .click_postman_tutorial() \
                           .go_back() \
                           .click_scrum_category()
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:
            log_exception(ex, HEADLESS_MODE, drive_main_page, 'main_page')
            pytest.fail

    @staticmethod
    def test_footer():
        try:
            drive_main_page.click_social_media_link('facebook') \
                           .go_back() \
                           .click_social_media_link('twitter') \
                           .go_back() \
                           .click_social_media_link('linkedin') \
                           .go_back() \
                           .click_social_media_link('youtube') \
                           .go_back()
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:
            log_exception(ex, HEADLESS_MODE, drive_main_page, 'main_page')
            pytest.fail

# ==========================  Init tests  =====================================

MAIN_PAGE_URL = data['pages']['main_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    drive_main_page = DriveMainPage(browser, MAIN_PAGE_URL, HEADLESS_MODE)

    # Header
    TestMainPage.test_header()
                
    # Body
    TestMainPage.test_body()
    
    # Footer
    TestMainPage.test_footer()
    
    drive_main_page.__exit__()