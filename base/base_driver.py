import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def scroll_To_infinitepage(self):
        driver = self.driver
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(4)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        time.sleep(10)

    def wait_until_element_to_be_clickable(self, locatortype, locator):
        element = self.wait.until(EC.element_to_be_clickable((locatortype, locator)))
        return element

    def wait_until_presence_of_all_elements_located(self, locatortype, locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locatortype, locator)))
        return list_of_elements

    def demo_find_elements(self, locatortype, locator):
        list_of_elements = self.driver.find_elements(locatortype, locator)
        return list_of_elements

    def demo_find_element(self, locatortype, locator):
        element = self.driver.find_element(locatortype, locator)
        return element
