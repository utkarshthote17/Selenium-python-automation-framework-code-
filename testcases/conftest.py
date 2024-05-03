import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup(request, browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get("https://www.yatra.com")
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("https://www.yatra.com")
    # request.cls.driver = driver
    # yield
    # driver.close()
