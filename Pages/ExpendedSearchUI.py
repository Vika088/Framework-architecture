from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Search:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.kinopoisk.ru/')
        self._wait_popup = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[5]/div/div/div/div[1]/div[2]/button[2]')))
        self._click_popup = (self._driver.find_element
                             (By.XPATH, '/html/body/div[5]/div/div/div/div[1]/div[2]/button[2]').click())
        self._driver.maximize_window()
        self._driver.implicitly_wait(20)

    def search_by_name(self):
        self._exp_search_button = self._driver.find_element(By.XPATH, "//a[@aria-label='Расширенный поиск']").click()
        self._find_film = self._driver.find_element(By.ID, 'find_film').send_keys('John Wick')
        self._wait_but = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@class='el_18 submit nice_button']")))
        self._click_but = self._driver.find_element(By.XPATH, "//input[@class='el_18 submit nice_button']").click()
        self._search_by_name_result = (self._driver.find_element
                                       (By.CLASS_NAME, 'search_results_topText').text.strip().replace
                                       ('поиск: John Wick • результаты: ', ''))
        print(self._search_by_name_result)
        return int(self._search_by_name_result)

    def search_by_year(self):
        self._exp_search_button = self._driver.find_element(By.XPATH, "//a[@aria-label='Расширенный поиск']").click()
        self._find_film_by_year = self._driver.find_element(By.ID, 'year').send_keys('1996')
        self._wait_but = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@class='el_18 submit nice_button']")))
        self._click_but = self._driver.find_element(By.XPATH, "//input[@class='el_18 submit nice_button']").click()
        self._search_by_year_result = (self._driver.find_element
                                       (By.CLASS_NAME, 'search_results_topText').text.strip().replace
                                       ('поиск: • результаты: ', ''))
        print(self._search_by_year_result)
        return int(self._search_by_year_result)

    def search_by_country(self):
        self._exp_search_button = self._driver.find_element(By.XPATH, "//a[@aria-label='Расширенный поиск']").click()
        self._find_film_by_country = (self._driver.find_element(By.ID, 'country')
                                      .find_element(By.XPATH, '//*[@id="country"]/option[43]').click())
        self._wait_but = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@class='el_18 submit nice_button']")))
        self._click_but = self._driver.find_element(By.XPATH, "//input[@class='el_18 submit nice_button']").click()
        self._search_by_country_result = self._driver.find_element(By.XPATH,
            '//*[@id="block_left_padtop"]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/h1/font').text
        print(self._search_by_country_result)
        return str(self._search_by_country_result)

    def search_by_genre(self):
        self._exp_search_button = self._driver.find_element(By.XPATH, "//a[@aria-label='Расширенный поиск']").click()
        self._find_film_by_genre = self._driver.find_element(By.XPATH, '//*[@id="m_act[genre]"] / option[7]').click()
        self._wait_but = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@class='el_18 submit nice_button']")))
        self._click_but = self._driver.find_element(By.XPATH, "//input[@class='el_18 submit nice_button']").click()
        self._search_by_genre_result = (self._driver.find_element
                                       (By.CLASS_NAME, 'search_results_topText').text.strip().replace
                                       ('поиск: • результаты: ', ''))
        print(self._search_by_genre_result)
        return int(self._search_by_genre_result)

    def search_by_rental_company(self):
        self._exp_search_button = self._driver.find_element(By.XPATH, "//a[@aria-label='Расширенный поиск']").click()
        self._rental_company = self._driver.find_element(By.XPATH, '//*[@id="company"]/option[62]').click()
        self._wait_but = WebDriverWait(self._driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@class='el_18 submit nice_button']")))
        self._click_but = self._driver.find_element(By.XPATH, "//input[@class='el_18 submit nice_button']").click()
        self._search_by_rental_company = (self._driver.find_element
                                       (By.CLASS_NAME, 'search_results_topText').text.strip().replace
                                       ('поиск: • результаты: ', ''))
        print(self._search_by_rental_company)
        return int(self._search_by_rental_company)
