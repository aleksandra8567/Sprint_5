from selenium.webdriver.support import expected_conditions as EC
from locators import AuthRegistre, AuthLogin
from utils import generate_email, generate_password


class TestRegistration:
    def setup_method(self):
        self.email = generate_email("shevtsova", "aleksandra", "qa-fs")
        self.password = generate_password(8)

    def test_successful_registration(self, driver, wait):
        #Проверяет успешную регистрацию с валидными данными
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.presence_of_element_located(AuthRegistre.ar_name_field))

        name_field = wait.until(EC.visibility_of_element_located(AuthRegistre.ar_name_field))
        name_field.clear()
        name_field.send_keys("Aleksandra")

        email_field = wait.until(EC.visibility_of_element_located(AuthRegistre.ar_email_field))

        email_field.clear()
        email_field.send_keys(self.email)

        password_field = wait.until(EC.visibility_of_element_located(AuthRegistre.ar_password_field))

        password_field.clear()
        password_field.send_keys(self.password)

        register_submit = wait.until(EC.element_to_be_clickable(AuthRegistre.ar_register_button))
        driver.execute_script("arguments[0].scrollIntoView();", register_submit)
        register_submit.click()

        wait.until(EC.presence_of_element_located(AuthLogin.al_login_text))
        current_url = driver.current_url.lower()
        assert "login" in current_url, f"Ожидалось 'login' в URL, но получил {current_url}"

    def test_invalid_password_error(self, driver, wait):
        #Проверяет отображение ошибки при некорректном пароле (менее 6 символов)
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.presence_of_element_located(AuthRegistre.ar_name_field))

        name_field = wait.until(EC.visibility_of_element_located(AuthRegistre.ar_name_field))
        name_field.clear()
        name_field.send_keys("Aleksandra")

        email_field = wait.until(EC.visibility_of_element_located(AuthRegistre.ar_email_field))

        email_field.clear()
        email_field.send_keys(self.email)

        password_field = wait.until(EC.visibility_of_element_located(AuthRegistre.ar_password_field))

        short_password = "12345"
        password_field.clear()
        password_field.send_keys(short_password)

        wait.until(EC.visibility_of_element_located(AuthRegistre.ar_name_field)).click()

        error_message = wait.until(EC.presence_of_element_located(AuthRegistre.ar_error_message))
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"
        assert len(error_message.text) > 0, "Текст сообщения об ошибке пуст"