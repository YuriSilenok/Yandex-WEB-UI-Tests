"""Implements classes for controls the search in multiple search categories."""
from selenium.webdriver.common.keys import Keys

from pages.base import BasePage
from locators.yandex.search import search
from locators.yandex.search import search_result
from locators.yandex.search import suggestions


class Search(BasePage):
    """Controls the search in the any category."""

    def __init__(self, browser):
        """Pass links to the browser \
and the class with locators to the parent constructor.

        Args:
            browser (WebDriver): a reference to an instance of the browser.
        """
        super().__init__(
            browser=browser,
            locators=search
        )

    def set_search(self, text: str):
        """Set the text in the search field."""
        self.find_element(
            locator=self.locators.INP_SEARCH,
            message="The search input is not found"
        ).send_keys(text)

    def get_search_value(self):
        """Get a value from the search field."""
        return self.find_element(
            locator=self.locators.INP_SEARCH,
            message="The search result table is not found."
        ).get_attribute('value')

    def push_enter(self):
        """Press enter keyboard."""
        self.find_element(self.locators.INP_SEARCH).send_keys(Keys.ENTER)


class Suggestions(BasePage):
    """Controls the live search."""

    def __init__(self, browser):
        """Pass links to the browser \
and the class with locators to the parent constructor.

        Args:
            browser (WebDriver): a reference to an instance of the browser.
        """
        super().__init__(
            browser=browser,
            locators=suggestions
        )

    def get_suggestions(self):
        """Get a list of suggest."""
        self.find_element(
            locator=self.locators.CONTAINER,
            message='The suggestions table is not found.')
        suggestions = self.browser.find_elements(*self.locators.LBL_SUGGEST)
        return [suggest.text for suggest in suggestions]


class SearchResult(BasePage):
    """Controls the search result."""

    def __init__(self, browser):
        """Pass links to the browser \
and the class with locators to the parent constructor.

        Args:
            browser (WebDriver): a reference to an instance of the browser.
        """
        super().__init__(
            browser=browser,
            locators=search_result
        )

    def get_header_links(self):
        """Get a list of header links."""
        self.find_element(
            locator=self.locators.CONTAINER,
            message='The search result table is not found.')
        result_header_links = self.browser.find_elements(
            *self.locators.LBL_HEADER_LINKS)
        return [link.get_attribute('href') for link in result_header_links]
