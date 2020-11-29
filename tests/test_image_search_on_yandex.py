"""Test Suite for Yandex search."""
import pytest
import time

from pages.yandex.navigation import NavigationMenu
from pages.yandex.search import Search
from pages.yandex.images import SearchResult
from pages.yandex.images import MediaView
from pages.yandex.images import PopularRequest
from pages.yandex.images import compare_two_binary_streams


def test_image_on_yandex(browser):
    """Test case of image search."""
    # The "Images" link is present on the page
    # Click on the link
    NavigationMenu(browser).click_images_image()
    # Check that you went to on the url https://yandex.ru/images/
    current_url = browser.current_url
    expected_url = 'https://yandex.ru/images/'
    assert expected_url in current_url, \
        f'Unexpected url: "{current_url}". Expected url: {expected_url}'
    # Open 1 category, check that it opened, in the search for the correct text
    image_name = PopularRequest(browser).click_first_image()
    search_value = Search(browser).get_search_value()
    assert image_name == search_value, \
        f"""Unexpected search value: "{search_value}". \
Expected search value: {image_name}"""
    # Open the first image, check that it opened
    SearchResult(browser).click_first_image()
    # When you click the forward button, the image changes
    media_view = MediaView(browser)
    image1_src = media_view.get_image_src()
    image1_bytes = media_view.get_image_bytes()
    media_view.click_next()
    image2_src = media_view.get_image_src()
    image2_bytes = media_view.get_image_bytes()
    assert image1_src != image2_src, 'The image has not changed'
    differences, binary_len, _ = compare_two_binary_streams(
        image1_bytes, image2_bytes)
    assert differences > 0, 'The image has not changed'
    media_view.click_prev()
    image3_src = media_view.get_image_src()
    image3_bytes = media_view.get_image_bytes()
    assert image1_src == image3_src, 'Images are not equal'
    differences, binary_len, same_length = compare_two_binary_streams(
        image1_bytes, image3_bytes)
    assert same_length, 'Images of different sizes'
    assert differences == 0, \
        'The images differ by {} byte, which is {}%.'\
        .format(differences, round(differences / binary_len * 100, 2))
