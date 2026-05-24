from selenium.webdriver.support import expected_conditions as EC
from locators import MainPage, LKProfile, AuthLogin

class TestLogout:
    def test_logout_from_profile(self, driver, wait):
        #Проверяет выход по кнопке «Выйти» в личном кабинете
        email = "cfswerfa@swfdaf.ry"
        password = "awdawdaw"

        wait.until(EC.element_to_be_clickable(MainPage.mn_auth)).click()
        wait.until(EC.visibility_of_element_located(AuthLogin.al_email_field)).send_keys(email)
        wait.until(EC.visibility_of_element_located(AuthLogin.al_password_field)).send_keys(password)
        wait.until(EC.element_to_be_clickable(AuthLogin.al_login_button_any_forms)).click()

        wait.until(EC.element_to_be_clickable(MainPage.mn_profile_button)).click()

        logout_button = wait.until(EC.element_to_be_clickable(LKProfile.lk_logout_button))
        logout_button.click()

        wait.until(EC.presence_of_element_located(AuthLogin.al_login_text))

        current_url = driver.current_url.lower()
        assert "login" in current_url, f"Ожидался переход на /login, но URL: {current_url}"