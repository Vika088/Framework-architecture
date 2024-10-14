from selenium import webdriver
from Pages.ExpendedSearchUI import Search

driver = webdriver.Chrome()
search = Search(driver)

def test_ui_name():
    result_by_name = search.search_by_name()
    print(result_by_name)
    assert result_by_name != 0

def test_ui_year():
    result_by_year = search.search_by_year()
    print(result_by_year)
    assert result_by_year != 0

def test_ui_country():
    result_by_country = search.search_by_country()
    print(result_by_country)
    assert result_by_country != '(0)'

def test_ui_genre():
    result_by_genre = search.search_by_genre()
    print(result_by_genre)
    assert result_by_genre != 0

def test_ui_rental_company():
    result_by_rental_company = search.search_by_rental_company()
    print(result_by_rental_company)
    assert result_by_rental_company != 0