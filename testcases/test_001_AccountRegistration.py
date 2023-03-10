import os
import time

import pytest

from pageObjects.homePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AccountReg():
    baceURL = ReadConfig.getApplicationURL()
    logr = LogGen.loggen()


    pytest.mark.regression
    def test_account_reg(self, setup):
        logr = LogGen.loggen()

        self.logr.info("***** Test 001 Account Registration Started.. ****")
        self.driver = setup
        self.driver.get(self.baceURL)
        self.driver.maximize_window()
        #time.sleep(3)

        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickRegister()
        #time.sleep(3)

        self.logr.info("Proving customer details for registration")
        self.regpage = AccountRegistrationPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        self.email = randomString.random_string_generator() + '@gmail.com'
        self.regpage.setEmail(self.email)
        # self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        # self.regpage.setConfirmPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg = self.regpage.getconfirmationmsg()
        if self.confmsg == "Your Account Has Been Created!":
            self.logr.info("Account registration is passed..")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "/screenshots/" + "test_account_reg.png")
            self.logr.error("Account registration is failed.")
            self.driver.close()
            assert False
        self.logr.info("**** test_001_AccountRegistration finished *** ")
