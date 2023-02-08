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
    NAME_TEXT_FIELD = (By.XPATH, "//div[@data-qe='save-search-name']//input")
    SAVE_SEARCH_CONFIRMATION = (By.XPATH, "//button[@data-cy='dialog-save-search-button']")
    SAVE_AS_NEW_SEARCH_BTN = (By.XPATH, "//button[contains(text(), 'Save as new search')]")
    EMPTY_NAME_ERROR_MSG = (By.XPATH, "//p[contains(text(), 'You must give your search a name')]")

    def __init__(self, driver):
        super().__init__(driver)

    def filter_saved_searches(self, name):
        try:
            self.click(self.FILTER_FIELD)
            self.clear_text(self.FILTER_FIELD)
            self.fill_text(self.FILTER_FIELD, name)
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

    def get_search_title(self):
        return self.get_inner_text(self.SEARCH_RESULT_TITLE)

    def get_search_already_exist_message(self):
        return self.get_inner_text(self.SAVED_SEARCH_EXIST_TXT)

    def get_empty_name_field_error_message(self):
        try:
            self.clear_text(self.NAME_TEXT_FIELD)
            self.click(self.SAVE_SEARCH_CONFIRMATION)
            return self.get_inner_text(self.EMPTY_NAME_ERROR_MSG)
        except NoSuchElementException:
            pass

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
