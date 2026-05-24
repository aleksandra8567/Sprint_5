from selenium.webdriver.common.by import By

class MainPage:
    mn_profile_button = (By.XPATH, ".//p[text()='Личный Кабинет']")
    mn_auth = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    mn_constructor_button = (By.XPATH, ".//p[text()='Конструктор']")
    mn_logo = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")

    mn_sauces_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")
    mn_h_sauces = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")

    mn_bun_button = (By.XPATH, ".//span[text()='Булки']/parent::*")
    mn_h_bun = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")

    mn_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")
    mn_h_filling = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")

class AuthLogin:
   al_login_text = (By.XPATH, ".//h2[text()='Вход']")
   al_login_button_any_forms = (By.XPATH, ".//button[text()='Войти']")
   al_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")
   al_email_field = (By.XPATH, ".//input[@name='name']")
   al_password_field = (By.XPATH, ".//input[@name='Пароль']")
   al_element_with_login_text = (By.XPATH, ".//*[text() = 'Вход']")

class AuthRegistre:
    ar_name_field = (By.XPATH, ".//input[@name='name']")
    ar_email_field = (By.XPATH, ".//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
    ar_password_field = (By.XPATH, ".//input[@type='password' and @name='Пароль']")
    ar_register_button = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")
    ar_error_message = (By.XPATH, ".//p[contains(@class, 'input__error') and contains(@class, 'text_type_main-default')]")
    ar_error_message_2 = (By.XPATH, ".//div[contains(@class, 'Auth_login')]//p[contains(@class, 'input__error')]")
    ar_login_button = (By.XPATH, ".//a[contains(text(), 'Войти')]")

class AuthPassword:
    ap_login_text_with_href = (By.XPATH, ".//a[text()='Войти']")

class LKProfile:
     """Локаторы элементов на странице личного кабинета"""
     lk_logout_button = (By.XPATH, ".//button[contains(text(), 'Выход')]")

