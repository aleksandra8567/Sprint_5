import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPage


@pytest.fixture
def navigate_to_section(driver, wait):
    def _navigate_to_section(button_locator, header_locator, expected_text):
        section_button = wait.until(EC.element_to_be_clickable(button_locator))
        ActionChains(driver).move_to_element(section_button).click().perform()

        header = wait.until(EC.presence_of_element_located(header_locator))

        assert header.is_displayed(), f"Заголовок раздела «{expected_text}» не отображён на странице"
        assert expected_text in header.text, f"Неверный текст в заголовке раздела. Ожидалось «{expected_text}», получено «{header.text}»"

    return _navigate_to_section


class TestNavigationSections:

    def test_navigate_to_buns_section(self, driver, wait, navigate_to_section):
        navigate_to_section(
            MainPage.mn_bun_button,
            MainPage.mn_h_bun,
            "Булки"
        )

    def test_navigate_to_sauces_section(self, driver, wait, navigate_to_section):
        navigate_to_section(
            MainPage.mn_sauces_button,
            MainPage.mn_h_sauces,
            "Соусы"
        )

    def test_navigate_to_fillings_section(self, driver, wait, navigate_to_section):
        navigate_to_section(
            MainPage.mn_filling_button,
            MainPage.mn_h_filling,
            "Начинки"
        )