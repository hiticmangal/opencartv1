from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from typing import ClassVar


class MyAccountsPage:
    #driver: Chrome  # driver = ClassVar[Chrome]
    lnk_logout_xpath = "//a[@class='list-group-item'][normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def click_Logout(self):
        self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()
