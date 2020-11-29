"""The module stores classes with common functionality on pages."""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException


class BasePage():
    """This class must be the parent of all classes that implement page."""

    def __init__(self, browser, locators):
        """Save the browser link and create Action Chains.

        An attempt is made to wait for the container.
        Args:
            browser (WebDriver): a reference to an instance of the browser.
            locators (class): link to the class with locators for this page. 
        """
        self.browser = browser
        self.action = ActionChains(browser)
        self.locators = locators
        self.wait_load()

    def find_element(self, locator, wait=5, appearance=True, message=None):
        """Wait for the element to appear or disappear.

        Args:
            locator (tuple): Contains the method and argument for searching
                for an element.
            wait (int, optional): The number of seconds that the item will be
                searched for. Defaults to 5.
            appearance (bool, optional): If True, the element is expected to
                appear. If false, the element is expected to disappear.
                Defaults to True.
            message (str, optional): This message will be issued on assert
                checks

        Returns: WebElement or True or None:
            If an element is expected to appear and the element is found,
            WebElement is returned, otherwise None is returned. If the element
            is expected to disappear and it has disappeared, it returns True,
            otherwise it returns None
        """
        element = None
        try:
            sleep_and_wait = 0.125
            self.browser.implicitly_wait(sleep_and_wait)
            wd_wait = WebDriverWait(
                driver=self.browser,
                timeout=wait,
                poll_frequency=sleep_and_wait)
            until = wd_wait.until if appearance else wd_wait.until_not
            while True:
                try:
                    element = until(EC.element_to_be_clickable(locator))
                    element = element if appearance else True
                    break
                except StaleElementReferenceException:
                    # Dynamic content is everywhere.
                    pass
        except TimeoutException as ex:
            if message:
                raise AssertionError(message)
            else:
                raise AssertionError(ex.msg)
        finally:
            self.browser.implicitly_wait(self.browser.wait)
        if element is WebElement:
            self.action.move_to_element(element).perform()
        # print(wait, appearance, locator, element)
        return element

    def wait_load(self, wait=5, appearance=True):
        """Wait for the container to load.

        If the container field of the locator class exists,
        it is searched until the time expires or the condition occurs (appearance).
        Args:
            wait (int, optional): Waiting time in seconds. Defaults to 5.
            appearance (bool, optional): If True, the element is expected to
                appear. If false, the element is expected to disappear.
                Defaults to True.
        """
        if not hasattr(self.locators, 'CONTAINER'):
            return
        self.find_element(
            locator=self.locators.CONTAINER,
            wait=wait,
            appearance=appearance,
            message=f'Failed while waiting for the {self.__class__.__name__} container'
        )
