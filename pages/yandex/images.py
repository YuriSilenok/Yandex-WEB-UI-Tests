"""Implements classes for managing the image search page."""
from selenium.webdriver.common.keys import Keys

from pages.base import BasePage

from locators.yandex.images import popular_request
from locators.yandex.images import search_result
from locators.yandex.images import media_view


class PopularRequest(BasePage):
    """Controls the images for popular queries."""

    def __init__(self, browser):
        """Pass links to the browser \
and the class with locators to the parent constructor.

        Args:
            browser (WebDriver): a reference to an instance of the browser.
        """
        super().__init__(
            browser=browser,
            locators=popular_request
        )

    def click_first_image(self):
        """Click on the label of the first image.

        Pre-checks that the container has loaded,
        and after clicking, checks that the container has disappeared.
        """
        self.find_element(
            locator=self.locators.CONTAINER,
            message='The popular request container is not found'
        )
        search_label = self.find_element(
            locator=self.locators.LBL_SEARCH_TEXT,
            message='The popular request search label is not found'
        )
        search_text = search_label.text
        search_label.click()
        self.find_element(
            locator=self.locators.CONTAINER,
            appearance=False,
            message="The popular request container didn't disappear"
        )
        return search_text


class SearchResult(BasePage):
    """Controls the search images."""

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

    def click_first_image(self):
        """Click on the first image found."""
        self.find_element(
            locator=self.locators.LBL_IMAGE_LINK,
            message="Images is not found"
        ).click()


class MediaView(BasePage):
    """Controls the image viewing panel."""

    def __init__(self, browser):
        """Pass links to the browser \
and the class with locators to the parent constructor.

        Args:
            browser (WebDriver): a reference to an instance of the browser.
        """
        super().__init__(
            browser=browser,
            locators=media_view
        )

    def click_next(self):
        """Click on the "more" button to go to the next image."""
        current_src = self.get_image_src()
        self.find_element(
            locator=self.locators.BTN_NEXT_IMAGE,
            message="The next button is not found"
        ).click()
        self.find_element(
            locator=self.locators.get_image_src(current_src),
            appearance=False
        )

    def click_prev(self):
        """Click on the "less" button to go to the next image."""
        current_src = self.get_image_src()
        self.find_element(
            locator=self.locators.BTN_PREV_IMAGE,
            message="The prev button is not found"
        ).click()
        self.find_element(
            locator=self.locators.get_image_src(current_src),
            appearance=False
        )

    def get_image_src(self):
        """Get the resource of the current image."""
        return self.find_element(
            locator=self.locators.IMG_MEDIA_VIEW,
            message="The media view image is not found"
        ).get_attribute('src')

    def get_image_bytes(self):
        """Get the binary stream of the current image."""
        return self.find_element(
            locator=self.locators.IMG_MEDIA_VIEW,
            message="The media view image is not found"
        ).screenshot_as_png


def compare_two_binary_streams(bin1, bin2):
    """Compare two binary streams byte-by-byte.

    Args:
        bin1 (bytes list): The first thread
        bin2 (bytes list): Second stream

    Returns:
        tuple (int, int, bool):
            [0] - Number of mismatched bytes
            [1] - Number of bytes to compare
            [2] - True if the compared streams are of the same length.
    """
    differences = 0
    bin1_len, bin2_len = len(bin1), len(bin2)
    binary_len = min(bin1_len, bin2_len)
    for i in range(binary_len):
        if bin1[i] != bin2[i]:
            differences += 1
    return differences, binary_len, bin1_len == bin2_len
