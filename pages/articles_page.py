from selenium.webdriver.common.by import By


class ArticlesPage():
    _DRIVER = None

    def __init__(self, driver, URL):        
        self._DRIVER = driver
        self._DRIVER.implicitly_wait(3)
        self._DRIVER.get(URL)
        self._DRIVER.maximize_window()

    def get_articles(self):
        return self._DRIVER.find_elements(By.CLASS_NAME, 'article__title')
    
    def get_page_index(self, page_index):
        return self._DRIVER.find_element(By.XPATH, f'//a[@href="/articles/pages/{page_index}"]')