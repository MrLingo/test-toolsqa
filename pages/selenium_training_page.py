from selenium.webdriver.common.by import By


class SeleniumTrainingPage():
    _DRIVER = None

    def __init__(self, driver, URL):        
        self._DRIVER = driver
        self._DRIVER.implicitly_wait(3)
        self._DRIVER.get(URL)
        self._DRIVER.maximize_window()

    def get_faqs(self):
        return self._DRIVER.find_elements(By.CLASS_NAME, 'faqs__expand')
    
    def get_what_is_included_info(self):
        return self._DRIVER.find_elements(By.CLASS_NAME, 'included__count'), self._DRIVER.find_elements(By.CLASS_NAME, 'included__type')

    def get_already_enrolled_count(self):
        return self._DRIVER.find_element(By.CLASS_NAME, 'certificate__already-enrolled--count')