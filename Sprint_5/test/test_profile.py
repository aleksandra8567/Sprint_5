from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPage, LKProfile, AuthLogin


class TestStellarBurgersProfileForm:

    def test_click_profile_button_open_profile_form(self, driver, wait):
        #Открыть личный кабинет и проверить загрузку страницы (с предварительной авторизацией)

        driver.get("https://stellarburgers.education-services.ru/login")

        email_field = wait.until(EC.element_to_be_clickable(AuthLogin.al_email_field))
        email_field.clear()
        email_field.send_keys("cfswerfa@swfdaf.ry")

        password_field = wait.until(EC.element_to_be_clickable(AuthLogin.al_password_field))
        password_field.clear()
        password_field.send_keys("awdawdaw")

        login_button = wait.until(EC.element_to_be_clickable(AuthLogin.al_login_button_any_forms))
        login_button.click()

        wait.until(EC.element_to_be_clickable(MainPage.mn_profile_button))

        profile_button = wait.until(EC.element_to_be_clickable(MainPage.mn_profile_button))
        profile_button.click()

        logout_button = wait.until(EC.element_to_be_clickable(LKProfile.lk_logout_button))
        assert logout_button.is_displayed(), "Кнопка 'Выход' не отображена — страница ЛК не загрузилась"

    def test_click_constructor_button_show_constructor_form(self, driver, wait):
        #Переход из личного кабинета в конструктор при нажатии кнопки 'Конструктор'
        constructor_button = wait.until(EC.element_to_be_clickable(MainPage.mn_constructor_button))
        constructor_button.click()

        h1_element = wait.until(EC.presence_of_element_located((By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")))
        assert h1_element.text == 'Соберите бургер', f"Ожидался заголовок 'Соберите бургер', но получен {h1_element.text}"

    def test_click_logo_button_show_constructor_form(self, driver, wait):
        #Переход из личного кабинета в конструктор при нажатии на лого
        logo_button = wait.until(EC.element_to_be_clickable(MainPage.mn_logo))
        logo_button.click()

        h1_element = wait.until(EC.presence_of_element_located((By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")))
        assert h1_element.text == 'Соберите бургер', f"Ожидался заголовок 'Соберите бургер', но получен {h1_element.text}"