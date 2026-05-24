from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPage

class TestConstructorNavigation:
    def test_navigate_to_buns_section(self, driver, wait):
        bun_button = wait.until(EC.element_to_be_clickable(MainPage.mn_bun_button))
        ActionChains(driver).move_to_element(bun_button).click().perform()
        wait.until(EC.presence_of_element_located(MainPage.mn_h_bun))

    def test_navigate_to_sauces_section(self, driver, wait):
        sauces_button = wait.until(EC.element_to_be_clickable(MainPage.mn_sauces_button))
        ActionChains(driver).move_to_element(sauces_button).click().perform()
        wait.until(EC.presence_of_element_located(MainPage.mn_h_sauces))

    def test_navigate_to_fillings_section(self, driver, wait):
        filling_button = wait.until(EC.element_to_be_clickable(MainPage.mn_filling_button))
        ActionChains(driver).move_to_element(filling_button).click().perform()
        wait.until(EC.presence_of_element_located(MainPage.mn_h_filling))