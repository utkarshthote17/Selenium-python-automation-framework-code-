import pytest
import softest
from pages.yatraLaunchPage import LaunchPage
from utilities.utilities import Util
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchFlights(softest.TestCase):
    log = Util.Custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Util()


    # @file_data('../testdata/testdata.json')

    # @data(("New Delhi", "New York", "29/04/2024", 1))
    # @unpack
    # @data(*(Util.read_data_from_csv("C:\\pycharm-projects\\TestFramworkDemo\\testdata\\test_data1.csv")))
    # @unpack
    @data(*(Util.read_data_from_excel("C:\\pycharm-projects\\TestFramworkDemo\\testdata\\test_d.xlsx", "Sheet1")))
    @unpack
    def test_search_flights_1stop(self, departfrom, departto, departdate, stop):
        search_flight_result = self.lp.search_flights(departfrom, departto, departdate)
        self.lp.scroll_To_infinitepage()
        all_stops = search_flight_result.searchflightresults(stop)
        self.ut.asserListItems(all_stops, stop)



    # def test_search_flights_2_stop(self):
    #     search_flight_result= self.lp.search_flights("New Delhi", "New York", "20/05/2024")
    #     self.lp.scroll_To_infinitepage()
    #     all_stops = search_flight_result.searchflightresults("2")
    #     print(len(all_stops))
    #     self.ut.asserListItems(all_stops, "2 Stops ")

#==================================== MAIN Execution method================================
