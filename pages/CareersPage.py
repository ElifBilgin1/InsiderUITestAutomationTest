import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.OpenPositionsPage import JobsPage
from locators.CareersPageLocators import CareersObjects


class CareersPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_qa_jobs(self):
        see_all_teams = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CareersObjects.all_teams_elem))
        )
        time.sleep(1)
        self.driver.execute_script(CareersObjects.scroll_into_view_script, see_all_teams)
        time.sleep(1)
        self.driver.execute_script(CareersObjects.scroll_up_script)
        time.sleep(1)
        see_all_teams.click()
        time.sleep(2)
        qa_team = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CareersObjects.qa_team_elem))
        )
        time.sleep(1)
        self.driver.execute_script(CareersObjects.scroll_into_view_script, qa_team)
        time.sleep(1)
        self.driver.execute_script(CareersObjects.scroll_up_script)
        time.sleep(1)
        qa_team.click()
        time.sleep(2)

        see_all_jobs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, CareersObjects.all_jobs_elem))
        )
        time.sleep(1)
        self.driver.execute_script(CareersObjects.scroll_into_view_script, see_all_jobs)
        time.sleep(1)
        self.driver.execute_script(CareersObjects.scroll_up_script)
        time.sleep(1)
        see_all_jobs.click()
        time.sleep(2)

        return JobsPage(self.driver)