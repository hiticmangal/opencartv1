import os
import time

import pytest

from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.homePage import HomePage
from pageObjects.login_page import LoginPage


class Test_Login():
    baseURL = ReadConfig.getApplicationURL()
    logr = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logr.info("########## Beginning Login Test ############")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.loginpg = LoginPage(self.driver)
        self.loginpg.setEmail(ReadConfig.getUseremail())
        self.loginpg.setPassword(ReadConfig.getPassword())
        print(ReadConfig.getPassword())
        self.loginpg.clickLogin()
        time.sleep(5)
        if self.loginpg.isMyAccountOpen():
            self.logr.info("######### Login Successful ############")
            assert True

        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "/screenshots/" + "test_login.png")
            self.logr.error("Login is failed.")

            assert False
        self.driver.close()
        self.logr.info("########## Login Failed #########")
