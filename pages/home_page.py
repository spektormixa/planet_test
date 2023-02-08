from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from actions.actions import Actions
import time


class HomePage(Actions):
    """Methods used in Planet Express Home Page."""

    SKIP_TOUR_BTN = (By.XPATH, "//button[@data-qe='skip-tour-button']")
    SEARCH_INPUT_FIELD = (By.XPATH, "//input[@data-qe='search-input']")
    SAVED_SEARCH_ICON = (By.XPATH, "//button[@data-qe='toggle-saved-searches']")

    def __init__(self, driver):
        super().__init__(driver)

    def skip_tour(self):
        try:
            self.click(self.SKIP_TOUR_BTN)
        except NoSuchElementException:
            pass

    def search_location(self, location):
        try:
            self.click(self.SEARCH_INPUT_FIELD)
            self.fill_text(self.SEARCH_INPUT_FIELD, location)
            time.sleep(1.5)  # Need for stability
            self.click_enter_key(self.SEARCH_INPUT_FIELD)
        except NoSuchElementException:
            pass

    # TODO: Remove code in try except block when Defect is fixed.
    def toggle_saved_searches(self):
        self.click(self.SAVED_SEARCH_ICON)
        try:
            reload_btn = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Reload')]"))
            )
            reload_btn.click()
        except Exception as e:
            pass
