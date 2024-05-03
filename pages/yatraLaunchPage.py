from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from base.base_driver import BaseDriver
from pages.searchFlightsPage import SearchFlightResult
from utilities.utilities import Util


class LaunchPage(BaseDriver):

    log = Util.Custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    DepartFromField = "//input[@id='BE_flight_origin_city']"
    DepartToField = "//input[@id='BE_flight_arrival_city']"
    DepartToLocationslocator = "//div[@class='viewport']//div[1]/li"
    DepartLocationFulName = "New York (NYC)"
    DepartureDateField = "//input[@id='BE_flight_origin_date']"
    DatesLocator = "//div[@id='monthWrapper']//tbody//td"
    SearchButton = "(//input[@id='BE_flight_flsearch_btn'])[1]"


    def demo_departfromfield(self):
        return self.demo_find_element(By.XPATH, self.DepartFromField)

    def enter_departfromlocation(self, departfrom):
        d_from = self.demo_departfromfield()
        d_from.click()
        sleep(3)
        d_from.send_keys(departfrom)
        sleep(3)
        d_from.send_keys(Keys.ENTER)


    def demo_departTofield(self):
        return self.demo_find_element(By.XPATH, self.DepartToField)

    def enter_departTolocation(self, departto):
        d_To = self.demo_departTofield()
        d_To.click()
        sleep(2)
        d_To.send_keys(departto)
        sleep(5)

        self.wait_until_element_to_be_clickable(By.XPATH, self.DepartToLocationslocator)
        search_results = self.demo_find_elements(By.XPATH, self.DepartToLocationslocator)
        print(len(search_results))
        for i in search_results:
            self.log.info(i.text)
            if self.DepartLocationFulName in i.text:
                self.log.info(i.text)
                i.click()
                break


    def demo_departuredatefield(self):
        return self.wait_until_element_to_be_clickable(By.XPATH, self.DepartureDateField)

    def selectdepartDate(self, departdate):

        elem = self.demo_departuredatefield()
        elem.click()
        elem1 = self.wait_until_element_to_be_clickable(By.XPATH, self.DatesLocator)
        dd_date = self.demo_find_elements(By.XPATH, self.DatesLocator)

        for i in dd_date:
            if i.get_attribute("data-date") == departdate:
                self.log.info(i.get_attribute("data-date"))
                i.click()
                sleep(3)
                break

    def click_searchButton(self):
        searchButton = self.demo_find_element(By.XPATH, self.SearchButton)
        searchButton.click()
        sleep(5)



    def search_flights(self,departfrom, departto, departdate):
        self.enter_departfromlocation(departfrom)
        self.enter_departTolocation(departto)
        self.selectdepartDate(departdate)
        self.click_searchButton()
        search_flight_result = SearchFlightResult(self.driver)
        return search_flight_result


#===============================================Unused Code=========================================



 # def depart_To(self, departto):
    #     going_To = self.demo_find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #     going_To.click()
    #     sleep(2)
    #     going_To.send_keys(departto)
    #     sleep(3)
    #
    #     self.wait_until_element_to_be_clickable(By.XPATH, self.DepartToLocationslocator)
    #     search_results = self.demo_find_elements(By.XPATH, self.DepartToLocationslocator)
    #     print(len(search_results))
    #     for i in search_results:
    #         print(i.text)
    #         if self.DepartLocationFulName in i.text:
    #             print(i.text)
    #             i.click()
    #             break