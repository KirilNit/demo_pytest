import pytest
from selenium import webdriver
from pages.notes_page import Notes_Page


@pytest.fixture(scope='class')
def invoke(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('w3c', False)
    _driver = webdriver.Chrome(options=options)
    request.cls._driver = _driver
    yield
    _driver.close()

@pytest.mark.usefixtures('invoke')
@pytest.fixture(scope='class')
def init_notes_page(request):
    notespage = Notes_Page(request.cls._driver)
    request.cls.notespage = notespage
    yield

# @pytest.fixture(scope='session', autouse=True)
# def close(request, driver):
#     def fin():
#         driver.quit()
#     request.addfinalizer()