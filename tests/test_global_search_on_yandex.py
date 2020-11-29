"""Test Suite for Yandex search."""
import pytest
import time

from pages.yandex.search import Search
from pages.yandex.search import SearchResult
from pages.yandex.search import Suggestions


def test_global_search_on_yandex(browser):
    """Test case of global search."""
    # Check whether the search field is available
    # Enter a Tensor in the search
    search = Search(browser)
    search_text = 'Тензор'
    search.set_search(search_text)
    # Check that the table with suggestions has appeared (suggest)
    suggestions = Suggestions(browser).get_suggestions()
    suggestions_len = len(suggestions)
    assert suggestions_len > 0, 'The suggestions list is empty.'
    search_text = search_text.lower()
    for i in range(min(suggestions_len, 5)):
        assert search_text in suggestions[i], \
            f"""The phrase "Tensor" was not found \
in the "{suggestions[i]}" suggest."""
    # When you press Enter, a table of search results appears
    # The first 5 results have a link to tensor.ru
    search.push_enter()
    header_links = SearchResult(browser).get_header_links()
    header_links_len = len(header_links)
    for i in range(min(header_links_len, 5)):
        assert 'tensor.ru' in header_links[i], \
            f"""The tensor.ru is not found \
in the {header_links[i]} search result header link"""
