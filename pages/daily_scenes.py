from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from actions.actions import Actions


class DailyScenes(Actions):
    """Methods used in Planet Express Daily Scenes."""

    SAVE_SEARCH_BTN = (By.XPATH, "//button[@data-qe='click-save-search-button']")
    NO_RESULTS_ERROR = (By.XPATH, "//h6[contains(text(), 'Sorry, no results found')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_save_update_search(self):
        try:
            self.click(self.SAVE_SEARCH_BTN)
        except NoSuchElementException:
            pass

    def get_error_title(self):
        try:
            return self.get_inner_text(self.NO_RESULTS_ERROR)
        except NoSuchElementException:
            pass
