import pytest
from selenium import webdriver
from utilities.base import Base
from pages.home_page import HomePage
from pages.login_page import LoginPage
from helper import properties
driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path=Base.ROOT_PATH + "/resources/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=Base.ROOT_PATH + "/resources/geckodriver")

    driver.get(properties.get_settings()['DEFAULT-BASE-URL'])

    driver.maximize_window()
    request.cls.driver = driver

    home = HomePage(driver)
    login = LoginPage(driver)

    # Setup
    user_login = properties.get_settings()['USER-LOGIN']
    password = properties.get_settings()['USER-PASSWORD']

    login.sign_in_to_app(user_login, password)
    home.skip_tour()
