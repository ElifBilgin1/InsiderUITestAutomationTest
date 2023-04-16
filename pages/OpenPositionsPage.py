import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.OpenPositionsPageLocators import JobsObjects


class JobsPage:
    def __init__(self, driver):
        self.driver = driver

    def filter_jobs(self):
        location_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, JobsObjects.location_filter_elem))
        )
        location_filter.click()
        time.sleep(2)

        location = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, JobsObjects.location_elem))
        )
        time.sleep(1)
        location.click()
        time.sleep(1)

        department_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, JobsObjects.department_filter_elem))
        )
        department_filter.click()
        time.sleep(1)

        department = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, JobsObjects.department_elem))
        )
        time.sleep(1)
        department.click()
        time.sleep(1)
        return self

    def get_jobs(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, JobsObjects.all_jobs_elem))
        )

