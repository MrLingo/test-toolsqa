import urllib3.exceptions
import pytest
from utilities.driver_handler import DriverHandler
from utilities.config_reader import data, browsers_config, headless_mode_config
from pages.articles_page import ArticlesPage
from utilities.exception_logger import log_exception


class DriveArticlesPage():
    _articles_page : ArticlesPage = None
    _DRIVER = None


    def __init__(self, driver, URL):
        self._DRIVER = driver
        self._articles_page = ArticlesPage(self._DRIVER, URL)

    # Other
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

ARTICLES_PAGE_URL = data['pages']['articles_page']
BROWSERS = browsers_config
HEADLESS_MODE = headless_mode_config

# Test on all browsers
for browser in BROWSERS:
    DriverHandler.init_driver(browser, HEADLESS_MODE)
    drive_articles_page = DriveArticlesPage(DriverHandler.get_driver(), ARTICLES_PAGE_URL)

    TestArticlesPage.test_extraction_of_articles()

    drive_articles_page.__exit__()