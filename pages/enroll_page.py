from selenium.webdriver.common.by import By


class EnrollPage():
    _DRIVER = None


    def __init__(self, driver, URL):        
        self._DRIVER = driver
        self._DRIVER.implicitly_wait(3)
        self._DRIVER.get(URL)
        self._DRIVER.maximize_window()

    # Form
    def get_first_name_field(self):
        return self._DRIVER.find_element(By.ID, 'first-name')

    def get_last_name_field(self):
        return self._DRIVER.find_element(By.ID, 'last-name')

    def get_email_field(self):
        return self._DRIVER.find_element(By.ID, 'email')

    def get_mobile_field(self):
        return self._DRIVER.find_element(By.ID, 'mobile')

    def get_country_field(self, country_input):
        self._DRIVER.find_element(By.ID, 'country').click()
        countries = self._DRIVER.find_elements(By.TAG_NAME, 'option')
        for country in countries:
            if country_input.lower() in country.get_attribute('innerHTML').lower():
                return country

        return self._DRIVER.find_element(By.ID, 'country')

    def get_city_field(self):
        return self._DRIVER.find_element(By.ID, 'city')

    def get_message_field(self):
        return self._DRIVER.find_element(By.ID, 'message')

    # OCR?
    def get_code_field(self):
        #self._DRIVER.find_element(By.CLASS_NAME, 'upcoming__registration--captcha')
        return self._DRIVER.find_element(By.ID, 'code')