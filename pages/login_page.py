from selenium.webdriver.common.by import By
from actions.actions import Actions


class LoginPage(Actions):
    """Methods used in Planet Express Login Page."""

    USERNAME_FIELD = (By.ID, "idp-discovery-username")
    PASSWORD_FIELD = (By.ID, "okta-signin-password")
    NEXT_BUTTON = (By.ID, "idp-discovery-submit")
    SIGN_IN_BUTTON = (By.ID, "okta-signin-submit")

    def __init__(self, driver):
        super().__init__(driver)

    def sign_in_to_app(self, email, password):
        self.click(self.USERNAME_FIELD)
        self.fill_text(self.USERNAME_FIELD, email)
        self.click(self.NEXT_BUTTON)
        self.click(self.PASSWORD_FIELD)
        self.fill_text(self.PASSWORD_FIELD, password)
        self.click(self.SIGN_IN_BUTTON)
