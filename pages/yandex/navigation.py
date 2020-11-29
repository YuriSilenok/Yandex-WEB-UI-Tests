"""Implements classes for controls the navigation menu."""
from selenium.webdriver.common.keys import Keys

from pages.base import BasePage

from locators.yandex.navigation import navigation_menu


class NavigationMenu(BasePage):
    """Controls the search category menu."""

    def __init__(self, browser):
        """Pass links to the browser \
and the class with locators to the parent constructor.

        Args:
            browser (WebDriver): a reference to an instance of the browser.
        """
        super().__init__(
            browser=browser,
            locators=navigation_menu
        )

    def click_images_image(self):
        """Click on the image to go to the search category "Images"."""
        self.find_element(
            locator=self.locators.BTN_IMAGES_IMAGE,
            message="The images button is not found"
        ).click()
        self.browser.switch_to.window(self.browser.window_handles[-1])
