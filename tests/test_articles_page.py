import time
import json

from selenium import webdriver
from pages.articles_page import ArticlesPage

class TestArticlesPage():
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

        self._articles_page = ArticlesPage(self._DRIVER, URL)

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
    
    def click_page(self, page_index):
        self._articles_page.get_page_index(page_index).click()
        return self

    # Articles
    def extract_articles(self, pages=1, click_items=False):
        articles = self._articles_page.get_articles()
        for page in range(pages):
            for index, article in enumerate(articles):
                if not click_items:
                    print('Article title extracted', articles[index].text)
                else:                    
                    # Catch stale element
                    try:
                        print('Article clicked ', articles[index].text)                        
                        articles[index].click()
                        self.go_back()
                    except:                        
                        articles[index] = self._articles_page.get_articles()[index]
                        print('Article clicked', articles[index].text)
                        articles[index].click()
                        self.go_back()

            print(str(pages) + " ==== ", page)
            if page+1 >= 1:
                self.click_page(page+2)
        return self
    
    def __exit__(self):
        self._DRIVER.quit()


# ==========================  Init tests  =====================================

# Read configuration
config_file = open('config/config.json')
data = json.load(config_file)
config_file.close()

MAIN_PAGE_URL = data['pages']['articles_page']
BROWSERS = [browser for browser in data['browsers']]
HEADLESS_MODE = data['headless_mode']

# Test on all browsers
for browser in BROWSERS:
    _articles_page = TestArticlesPage(browser, MAIN_PAGE_URL, HEADLESS_MODE)
    
    _articles_page.extract_articles(False) \
                  .extract_articles(2, True)

    #_articles_page.__exit__()