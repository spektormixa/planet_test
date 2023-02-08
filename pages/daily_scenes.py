from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from actions.actions import Actions


class DailyScenes(Actions):
    """Methods used in Planet Express Daily Scenes."""

    SAVE_SEARCH_BTN = (By.XPATH, "//button[@data-qe='click-save-search-button']")
    NAME_TEXT_FIELD = (By.XPATH, "//div[@data-qe='save-search-name']//input")
    SAVE_SEARCH_CONFIRMATION = (By.XPATH, "//button[@data-cy='dialog-save-search-button']")
    NO_RESULTS_ERROR = (By.XPATH, "//h6[contains(text(), 'Sorry, no results found')]")
    SAVE_AS_NEW_SEARCH_BTN = (By.XPATH, "//button[contains(text(), 'Save as new search')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_save_update_search(self):
        try:
            self.click(self.SAVE_SEARCH_BTN)
        except NoSuchElementException:
            pass

    # TODO: Add enable Notifications
    def save_search_result(self, name, save_as_new=False):
        try:
            self.clear_text(self.NAME_TEXT_FIELD)
            self.fill_text(self.NAME_TEXT_FIELD, name)
            if not save_as_new:
                self.click(self.SAVE_SEARCH_CONFIRMATION)
            else:
                self.click(self.SAVE_AS_NEW_SEARCH_BTN)
        except NoSuchElementException:
            pass

    def get_error_title(self):
        try:
            return self.get_inner_text(self.NO_RESULTS_ERROR)
        except NoSuchElementException:
            pass
