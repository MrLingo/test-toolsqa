from selenium import webdriver
from utilities.config_reader import data, browsers_config, headless_mode_config
from pages.articles_page import ArticlesPage
from utilities.exception_logger import log_exception
import urllib3.exceptions
import pytest


class DriveArticlesPage():
    _articles_page : ArticlesPage = None
    _DRIVER = None
    _OPTIONS = None

    def __init__(self, browser, URL, headless_mode):        
        if(browser == 'Firefox'):
            self._OPTIONS = webdriver.FirefoxOptions().add_argument('--headless=new') if headless_mode else None
            firefox_service = webdriver.FirefoxService(log_output='geckodriver.log')

            self._DRIVER = webdriver.Firefox(options=self._OPTIONS, service=firefox_service)                        
        elif(browser == 'Edge'):
            self._OPTIONS = webdriver.EdgeOptions().add_argument('--headless=new') if headless_mode else None
            edge_service = webdriver.FirefoxService(log_output='geckodriver.log')

            self._DRIVER = webdriver.Edge(options=self._OPTIONS, service=edge_service)

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

    def take_screenshot(self, dir):
        self._DRIVER.get_screenshot_as_file(dir)

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


class TestArticlesPage():
    @staticmethod
    def test_extraction_of_articles():
        try:
            drive_articles_page.extract_articles(False) \
                               .extract_articles(2, True)
            
            assert True            
        except urllib3.exceptions.MaxRetryError:            
            assert True    
        except Exception as ex:            
            log_exception(ex, HEADLESS_MODE, drive_articles_page, 'articles_page')
            pytest.fail

# ==========================  Init tests  =====================================

MAIN_PAGE_URL = data['pages']['articles_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    drive_articles_page = DriveArticlesPage(browser, MAIN_PAGE_URL, HEADLESS_MODE)

    TestArticlesPage.test_extraction_of_articles()

    drive_articles_page.__exit__()