"""Selectors for the page https://yandex.ru/images/."""
from selenium.webdriver.common.by import By


class search_result:
    """Locators for search results."""

    CONTAINER = (By.CSS_SELECTOR, '.serp-list_type_search')
    LBL_IMAGE_LINK = (By.CSS_SELECTOR, '.serp-item a.serp-item__link')


class popular_request:
    """Locators for popular image queries."""

    CONTAINER = (By.CSS_SELECTOR, '.PopularRequestList')
    LBL_SEARCH_TEXT = (By.CSS_SELECTOR, '.PopularRequestList-SearchText')


class media_view:
    """Locators for the view image panel."""

    BTN_NEXT_IMAGE = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext')
    BTN_PREV_IMAGE = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev')
    IMG_MEDIA_VIEW = (By.CSS_SELECTOR, '.MMImage-Preview')

    @staticmethod
    def get_image_src(src: str):
        """Get a dynamic locator for an image with the specified src.

        Args:
            src (str): image url

        Returns:
            [tuple]: locator
        """
        return (By.XPATH, f'//img[@class="MMImage-Preview" and @src="{src}')
