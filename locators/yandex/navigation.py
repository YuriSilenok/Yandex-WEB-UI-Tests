"""Locators for any menu."""
from selenium.webdriver.common.by import By


class navigation_menu:
    """Locators for the navigation menu that controls search categories."""

    BTN_IMAGES_IMAGE = (By.CSS_SELECTOR, 'a[data-id=images]')
