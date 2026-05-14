from selenium.webdriver.common.by import By

class HomePage():
    lnk_myaccount_Xpath = "//a[@title ='My Account']"
    lnk_register_linktext = "Register"
    lnk_login_linktext = "Login"

    def __init__(self,driver):
        self.driver = driver

    def clickMYAccount(self):
        self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_register_linktext).click()

    def clickLogin(self):
        self.driver.find_element(By.LINK_TEXT,self.lnk_login_linktext).click()

