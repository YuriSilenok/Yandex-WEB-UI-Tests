# Yandex WEB UI Tests

Этот репозиторий реализует "[Тестовое задание на позицию разработчика в тестировании](docs/technical_specification/READMY.md)"

С технической документацией Вы можете ознакмиться в разделе [Wiki](https://github.com/YuriSilenok/Yandex-WEB-UI-Tests/wiki)


Ниже представлен отчет о выполнении тестировая

```
========================================================================================================================= test session starts ========================================================================================================================= 
platform win32 -- Python 3.8.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
rootdir: C:\Users\silen\Documents\GitHub\Yandex-WEB-UI-Tests
plugins: cov-2.9.0
collected 2 items                                                                                                                                                                                                                                                       

tests\test_global_search_on_yandex.py
DevTools listening on ws://127.0.0.1:51414/devtools/browser/be974a1a-d2b2-4442-84c4-98c0aaaf3687
F                                                                                                                                                                                                                           [ 50%]
tests\test_image_search_on_yandex.py .                                                                                                                                                                                                                           [100%] 

============================================================================================================================== FAILURES =============================================================================================================================== 
____________________________________________________________________________________________________________________ test_global_search_on_yandex _____________________________________________________________________________________________________________________ 

browser = <selenium.webdriver.chrome.webdriver.WebDriver (session="29d2bbd40d4ae7d9d33ec77e0009627a")>

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
>           assert 'tensor.ru' in header_links[i], \
                f"""The tensor.ru is not found \
    in the {header_links[i]} search result header link"""
E           AssertionError: The tensor.ru is not found in the https://vk.com/tensor_company search result header link
E           assert 'tensor.ru' in 'https://vk.com/tensor_company'

tests\test_global_search_on_yandex.py:32: AssertionError
======================================================================================================================= short test summary info ======================================================================================================================= 
FAILED tests/test_global_search_on_yandex.py::test_global_search_on_yandex - AssertionError: The tensor.ru is not found in the https://vk.com/tensor_company search result header link
==================================================================================================================== 1 failed, 1 passed in 24.98s =====================================================================================================================
```