"""For more information about this module, see here. \
https://docs.pytest.org/en/2.7.3/plugins.html."""
import pytest

from selenium import webdriver


START_LINK = 'https://yandex.ru'


@pytest.fixture(autouse=True, scope="function")
def go_to_home(browser):
    """go to the home page before each test case."""
    browser.get(START_LINK)

@pytest.fixture(scope="session")
def browser():
    """Open the browser once for all tests."""
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        browser = webdriver.Chrome(options=options)
        browser.wait = 5
        browser.implicitly_wait(browser.wait)
        yield browser
    finally:
        browser.quit()
