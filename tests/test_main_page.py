import time
import json

from selenium import webdriver
from pages.main_page import MainPage

class TestMainPage():
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

    # To switch handle
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


# ==========================  Init tests  =====================================

# Read configuration
config_file = open('config/config.json')
data = json.load(config_file)
config_file.close()

MAIN_PAGE_URL = data['pages']['main_page']
BROWSERS = [browser for browser in data['browsers']]
HEADLESS_MODE = data['headless_mode']

# Test on all browsers
for browser in BROWSERS:
    test_main_page = TestMainPage(browser, MAIN_PAGE_URL, HEADLESS_MODE)

    # Chain by section
    # Header
    test_main_page.click_logo_img() \
                  .click_home_nav_item() \
                  .click_selenium_train_nav_item()
     
    curr_window = test_main_page.get_current_window()
    
    test_main_page.click_demo_site_nav_item() \
                  .go_to_original_tab(curr_window) \
                  .click_about_nav_item() \
                  .type_into_search_field('testing input field')
                  
    # Body
    test_main_page.get_training_batch_announcment_text() \
                  .click_postman_tutorial() \
                  .go_back() \
                  .click_scrum_category()

    # Footer
    test_main_page.click_social_media_link('facebook') \
                  .go_back() \
                  .click_social_media_link('twitter') \
                  .go_back() \
                  .click_social_media_link('linkedin') \
                  .go_back() \
                  .click_social_media_link('youtube') \
                  .go_back()
    
    test_main_page.__exit__()