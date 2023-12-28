from selenium.webdriver.common.by import By


class AgileScrumPage():
    _DRIVER = None

    def __init__(self, driver, URL):        
        self._DRIVER = driver
        self._DRIVER.implicitly_wait(3)
        self._DRIVER.get(URL)
        self._DRIVER.maximize_window()

    def get_tutorial_release_date(self):
        return self._DRIVER.find_element(By.CLASS_NAME, 'article-meta-data__published-at')

    def get_author(self):
        return self._DRIVER.find_element(By.XPATH, '//div[@class="col-auto pr-0 article-meta-data__author--name"]')

    def get_reviewer(self):
        return self._DRIVER.find_element(By.XPATH, '//div[@class="col-auto pr-0 article-meta-data__reviewer--name"]')

    def get_comment_section(self):
        return self._DRIVER.find_element(By.CLASS_NAME, 'btn-block btn-load-comments btn-primary-outline lg')

    def get_next_lesson(self):
        return self._DRIVER.find_element(By.XPATH, '//div[@class="col text-right"]')