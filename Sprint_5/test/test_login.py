from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, AuthLogin, AuthRegistre, AuthPassword


class TestLogin:
    def test_login_from_main_page_button(self, driver, wait):
        #Проверяет, что по кнопке «Войти в аккаунт» на главной происходит переход на страницу входа
        auth_button = wait.until(EC.element_to_be_clickable(MainPage.mn_auth))
        driver.execute_script("arguments[0].scrollIntoView();", auth_button)
        auth_button.click()

        wait.until(EC.presence_of_element_located(AuthLogin.al_login_text))
        current_url = driver.current_url.lower()
        assert "login" in current_url, f"Ожидался переход на /login, но URL: {current_url}"

    def test_login_via_profile_link(self, driver, wait):
        #Проверяет, что по кнопке «Личный кабинет» происходит переход на страницу входа
        profile_button = wait.until(EC.element_to_be_clickable(MainPage.mn_profile_button))
        driver.execute_script("arguments[0].scrollIntoView();", profile_button)
        profile_button.click()

        wait.until(EC.presence_of_element_located(AuthLogin.al_login_text))
        current_url = driver.current_url.lower()
        assert "login" in current_url, f"Ожидался переход на /login, но URL: {current_url}"

    def test_login_from_registration_form(self, driver, wait):
        driver.get("https://stellarburgers.education-services.ru/register")

        login_button = wait.until(EC.element_to_be_clickable(AuthRegistre.ar_login_button))
        login_button.click()

        wait.until(EC.presence_of_element_located(AuthLogin.al_login_text))

        expected_url = "https://stellarburgers.education-services.ru/login"
        assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, но получен {driver.current_url}"

    def test_login_from_forgot_password_form(self, driver, wait):
        driver.get("https://stellarburgers.education-services.ru/forgot-password")

        login_button = wait.until(EC.element_to_be_clickable(AuthPassword.ap_login_text_with_href))
        login_button.click()

        wait.until(EC.presence_of_element_located(AuthLogin.al_login_text))

        expected_url = "https://stellarburgers.education-services.ru/login"
        assert driver.current_url == expected_url, f"Ожидался URL {expected_url}, но получен {driver.current_url}"