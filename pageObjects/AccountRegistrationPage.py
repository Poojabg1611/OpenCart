from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email = "email"
    txt_telephone = "telephone"
    txt_password = "password"
    txt_confirm_password = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath = "//input[@value= 'Continue']"
    text_msg_conf_xpath="//h1[normalixe-space()= 'your Account Has been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def __setFirstName(self,fname):
        self.driver.find_element_by_xpath(By.NAME,self.txt_firstname_name).send_keys(fname)

    def __setLastName(self,lname):
            self.driver.find_element_by_xpath(By.NAME,self.txt_lastname_name).send_keys(lname)

    def __setEmail(self,email):
        self.driver.find_element_by_xpath(By.NAME,self.txt_email).send_keys(email)

    def __setTelephone(self,tel):
        self.driver.find_element_by_xpath(By.NAME,self.txt_telephone).send_keys(tel)

    def __setPassword(self,pwd):
        self.driver.find_element_by_xpath(By.NAME,self.txt_password).send_keys(pwd)

    def __setConfirmPassword(self,cnfpwd):
        self.driver.find_element_by_xpath(By.NAME,self.txt_confirm_password).send_keys(cnfpwd)

    def setPrivacyPolicy(self):
        self.driver.find_element_by_xpath(By.NAME,self.chk_policy_name).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.bth_cont_xpath).click()

    def getconfimationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None

    def setFirstName(self, param):
        pass

    def setLastName(self, param):
        pass

    def getconfirmationmsg(self):
        pass

    def setPassword(self, param):
        pass

    def setTelephone(self, param):
        pass

    def setEmail(self, email):
        pass

    
    
            

