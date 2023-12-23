from selenium import webdriver
from pages.main_page import MainPage

class TestMainPage():
    _main_page = None
    _DRIVER = None

    def __init__(self, browser, URL):
        if(browser == 'Firefox'):
            self._DRIVER = webdriver.Firefox()
        elif(browser == 'Edge'):
            self._DRIVER = webdriver.Edge()

        self._main_page = MainPage(self._DRIVER, URL)

    # Other
    def go_to_original_tab(self, curr_window_handle):        
        handles = self._DRIVER.window_handles

        for window in handles:
            if window != curr_window_handle:
                self._DRIVER.switch_to.window(handles[0])
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
        self._main_page.get_search_bar().send_keys(text)
        return self
    
    def get_training_batch_announcment_text(self):
        print("Announcement text: ", self._main_page.get_training_batch_announcment_text())
        return self

    def click_cypress_tutorial(self):

        self._main_page.get_cypress_tutorial()
        return self

    # Body
    def click_enroll_button(self):
        enroll_element = self._main_page.get_enroll_button()
        if "enroll" in enroll_element.get_attribute('innerHTML').lower():
            enroll_element.click()
            return self
    
    def click_postman_tutorial(self):
        self._main_page.click_postman_tutorial()
        return self

    # To switch handle
    def click_latest_article_button(self):
        self._main_page.get_latest_articles_button().click()
        return self

    def click_scrum_category(self):
        self._main_page.get_scrum_learning_item().click()
        return self

    def __exit__(self):
        self._DRIVER.quit()

    
MAIN_PAGE_URL = 'https://toolsqa.com/'
BROWSERS = ['Firefox']
HEDLESS_MODE = False

# Test on all browsers
for browser in BROWSERS:
    test_main_page = TestMainPage(browser, MAIN_PAGE_URL)

    # Chain by section
    # Header
    test_main_page.click_logo_img() \
                  .click_home_nav_item() \
                  .click_selenium_train_nav_item() \
                  .click_cypress_tutorial()
     
    curr_window = test_main_page.get_current_window()
    
    test_main_page.click_demo_site_nav_item()
    test_main_page.go_to_original_tab(curr_window)
    test_main_page.click_about_nav_item()
            
    test_main_page.type_into_search_field('testing input field')
                  
    # Body
    test_main_page.get_training_batch_announcment_text() \
    .click_postman_tutorial() \
    .click_scrum_category()

    test_main_page.__exit__()