"""Locators for the page https://yandex.ru/."""
from selenium.webdriver.common.by import By


class search:
    """Locators for elements of the search."""

    INP_SEARCH = (By.CSS_SELECTOR, '.input__box>input[name=text]')


class suggestions:
    """Locators for live search."""

    CONTAINER = (By.XPATH, '//ul[contains(@id, "suggest-list")]')
    LBL_SUGGEST = (By.XPATH, '//li[contains(@id, "suggest-item")]')


class search_result:
    """Locators for search results."""

    CONTAINER = (By.CSS_SELECTOR, 'ul#search-result')
    LBL_HEADER_LINKS = (By.CSS_SELECTOR, 'ul#search-result>li h2>a')
