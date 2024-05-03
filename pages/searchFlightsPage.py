from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

from base.base_driver import BaseDriver
from utilities.utilities import Util


class SearchFlightResult(BaseDriver):
    log = Util.Custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    FilterButtonFor1stop = "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    AllFlightStopsLocatorfor1stop = "//span[contains(text(),'1 Stop ')]"
    FilterButtonFor2stop = "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    AllFlightStopsLocatorfor2stop = "//span[contains(text(),'2 Stops ')]"


    def demo_filterbuttonfor1stop(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.FilterButtonFor1stop)

    def demo_filterbuttonfor2stop(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.FilterButtonFor2stop)


    def select_flight_stop(self, stop):
        if stop == 1:
            button = self.demo_filterbuttonfor1stop()
            button.click()
            sleep(10)
        elif stop == 2:
            button = self.demo_filterbuttonfor2stop()
            button.click()
            sleep(10)




    def searchflightresults(self,stop):
        if stop == 1:
            self.select_flight_stop(stop)
            self.wait_until_presence_of_all_elements_located(By.XPATH, self.AllFlightStopsLocatorfor1stop)
            all_stops = self.demo_find_elements(By.XPATH, self.AllFlightStopsLocatorfor1stop)
            self.log.info(len(all_stops))
            return all_stops
        elif stop == 2:
            self.select_flight_stop(stop)
            self.wait_until_presence_of_all_elements_located(By.XPATH, self.AllFlightStopsLocatorfor2stop)
            all_stops = self.demo_find_elements(By.XPATH, self.AllFlightStopsLocatorfor2stop)
            self.log.info(len(all_stops))
            return all_stops






















