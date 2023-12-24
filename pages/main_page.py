from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage():
    _DRIVER = None

    def __init__(self, driver, URL):        
        self._DRIVER = driver
        self._DRIVER.implicitly_wait(3)
        self._DRIVER.get(URL)
        self._DRIVER.maximize_window()
        

    # Header           
    def get_nav_bar_item(self, item_idx):
        nav_bar = self._DRIVER.find_element(By.XPATH, '//ul[@class="navbar__links d-none d-lg-flex"]')
        return nav_bar.find_elements(By.TAG_NAME, 'li')[item_idx]
    
    def get_search_bar(self):
        try:
            return self._DRIVER.find_elements(By.CLASS_NAME, 'navbar__search--input')[1]
        except:
            return self._DRIVER.find_elements(By.CLASS_NAME, 'navbar__search--input')[0]
        

    # Body
    def get_scrum_learning_item(self):
        categories = self._DRIVER.find_elements(By.CLASS_NAME, 'category__name')
        for category in categories:
            if 'scrum' in category.get_attribute('innerHTML').lower():
                return category

    def get_logo_img(self):
        return self._DRIVER.find_element(By.CLASS_NAME, 'tools-qa-header__logo')

    def get_enroll_button(self):
        return self._DRIVER.find_element(By.XPATH, '//a[@href="/selenium-training?q=banner#enroll-form"]')
    
    def get_read_more_banner(self):
        return self._DRIVER.find_element(By.CLASS_NAME, 'new-training__read-more')

    def get_training_batch_announcment_text(self):
        return self._DRIVER.find_element(By.CLASS_NAME, 'new-training__starting').text
    
    # TO FINISH
    def get_cypress_tutorial(self):
        #tutorials_menu = self._DRIVER.find_element(By.XPATH, '//a[@class="navbar__tutorial-menu"]').click()
        menu_items = self._DRIVER.find_elements(By.TAG_NAME, 'span')
        for item in menu_items:
            print(item.text)
            if 'front' in item.text.lower():
                front_end_item = item
                front_end_item.click()
                
        # Need to specifiy via parents
        cypress_button = self._DRIVER.find_elements(By.XPATH, '//a[@href="/cypress-tutorial/"]')
        cypress_button = cypress_button[1]
        return cypress_button

    def get_postman_tutorial_redirect(self):
        tutorials = self._DRIVER.find_elements(By.CLASS_NAME, 'category__name')
        for tutorial in tutorials:
            if 'postman' in tutorial.text.lower():
                return tutorial

    def get_latest_articles_button(self):
        return self._DRIVER.find_element(By.XPATH, '//a[@href="/articles"]')

    # Footer
    def get_find_us_icon(self, social_media):
        anchors = self._DRIVER.find_elements(By.XPATH, '//a[@class="page-link-wrapper d-block"]')
        for social_media_icon in anchors:
            if social_media in social_media_icon.get_attribute('href').lower():
                return social_media_icon        