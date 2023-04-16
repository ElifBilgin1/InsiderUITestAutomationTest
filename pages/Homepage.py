import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CareersPage import CareersPage
from locators.HomepageLocators import HomeObjects


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(HomeObjects.url)
        return self

    def go_to_careers(self):
        more_menu = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, HomeObjects.more_menu_elem))
        )
        time.sleep(1)
        more_menu.click()

        careers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, HomeObjects.careers_elem))
        )
        time.sleep(1)
        careers.click()
        return CareersPage(self.driver)