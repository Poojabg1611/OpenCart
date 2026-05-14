from Utilies import randomString
from Utilies.readProperties import ReadConfig
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from Utilies.customLogger import LogGen
from datetime import datetime

class Test_001_AccountReg:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen() #logging

    def test_account_reg(self, setup):
        self.logger.info("**** test_001_AccountRegistration started **** ")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.driver.info("Launching application")
        self.driver.maximize_window()

        self.hp=HomePage(self.driver)
        self.logger.info("clicking on MyAccount --> register")
        self.hp.clickMYAccount()
        self.hp.clickRegister()

        self.logger.info("Providing customer details for registration")
        self.regpage=AccountRegistrationPage(self.driver)

        self.regpage.setFirstName("John")
        self.regpage.setLastName("Canedy")
        #self.regpage.setEmail("abc0951776091@gamil.com")
        self.email =randomString.random_String_generator()+'@gmail.com'
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("65656565")
        self.regpage.setPassword("abcxyz")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        self.confmsg=self.regpage.getconfirmationmsg()

        if self.confmsg=="Your Account has been created!":
            self.logger.info("Account created successfully")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshots(os.path.abspath(os.curdir)+"\\screenshots\\"+"test_account_reg.png")
            self.logger.info("Account creation failed")
            self.driver.close()
            assert False
        self.logger.info("**** test_001_AccountRegistration finished ****")