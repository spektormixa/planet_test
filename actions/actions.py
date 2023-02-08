from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
import time


class Actions:
    """ Wrapper for selenium operations """

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(self.driver, 10)

    def get_element(self, element):
        el = self._wait.until(expected_conditions.element_to_be_clickable(element))
        return el

    def click(self, element):
        el = self._wait.until(expected_conditions.element_to_be_clickable(element))
        el.click()

    def fill_text(self, element, txt):
        el = self._wait.until(expected_conditions.visibility_of_element_located(element))
        el.clear()
        el.send_keys(txt)

    def click_enter_key(self, element):
        el = self._wait.until(expected_conditions.visibility_of_element_located(element))
        el.send_keys(Keys.ENTER)

    def get_inner_text(self, element):
        el = self._wait.until(expected_conditions.element_to_be_clickable(element)).get_attribute('innerText')
        return el

    # TODO: Find out why  clear is not working by clear() function.
    def clear_text(self, element):
        el = self._wait.until(expected_conditions.element_to_be_clickable(element))
        time.sleep(1)
        el.send_keys(Keys.COMMAND, 'a')
        el.send_keys(Keys.BACKSPACE)

    def refresh_page(self):
        self.driver.refresh()

