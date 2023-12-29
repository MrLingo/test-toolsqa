from selenium import webdriver

class DriverHandler():
     _DRIVER = None
     _OPTIONS = None

     def init_driver(browser, headless_mode):        
        if(browser == 'Firefox'):
            DriverHandler._OPTIONS = webdriver.FirefoxOptions().add_argument('--headless=new') if headless_mode else None
            firefox_service = webdriver.FirefoxService(log_output='geckodriver.log')

            DriverHandler._DRIVER = webdriver.Firefox(options=DriverHandler._OPTIONS, service=firefox_service)                        
        elif(browser == 'Edge'):
            DriverHandler._OPTIONS = webdriver.EdgeOptions().add_argument('--headless=new') if headless_mode else None
            edge_service = webdriver.EdgeService(log_output='geckodriver.log')

            DriverHandler._DRIVER = webdriver.Edge(options=DriverHandler._OPTIONS, service=edge_service)
    
     @staticmethod
     def get_driver():
        return DriverHandler._DRIVER