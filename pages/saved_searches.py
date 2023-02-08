import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from actions.actions import Actions


class SavedSearches(Actions):
    """Methods used in Planet Express Saved Searches."""

    FILTER_FIELD = (By.XPATH, "//input[@placeholder='Filter by name']")
    SEARCH_RESULT_TITLE = (By.XPATH, "//li[@data-qe='search-list-item']//h6[@data-qe='search-list-item-title']")
    DELETE_ICON = (By.XPATH, "//button[@data-qe='menu-search-item-delete']")
    SAVED_SEARCH_EXIST_TXT = (By.XPATH, "//p[contains(text(), 'A saved search already exists with that name')]")
    CLOSE_DIALOG_ICON = (By.XPATH, "//button[@data-qe='dialog-close-button']")

    def __init__(self, driver):
        super().__init__(driver)

    def filter_saved_searches(self, name):
        try:
            self.click(self.FILTER_FIELD)
            self.clear_text(self.FILTER_FIELD)
            self.fill_text(self.FILTER_FIELD, name)
        except NoSuchElementException:
            pass

    def get_search_title(self):
        return self.get_inner_text(self.SEARCH_RESULT_TITLE)

    def get_search_already_exist_message(self):
        return self.get_inner_text(self.SAVED_SEARCH_EXIST_TXT)

    def click_saved_search(self):
        try:
            self.click(self.SEARCH_RESULT_TITLE)
            time.sleep(1)  # Need for Stability
        except NoSuchElementException:
            pass

    def delete_saved_search(self):
        try:
            self.click(self.DELETE_ICON)
        except NoSuchElementException:
            pass

    def click_close_save_search_dialog(self):
        try:
            self.click(self.CLOSE_DIALOG_ICON)
        except NoSuchElementException:
            pass
