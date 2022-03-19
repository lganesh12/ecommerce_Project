from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword
    #logger = logGen.custom_logger()


    def test_pageTitle(self,setup):

        # self.logger.info("****************Test_001_Login**********************")
        # self.logger.info("********Verifying Home Page Title ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            #self.logger.info("*************Home Page title test is passed **********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_pageTitle.png")
            self.driver.close()
            #self.logger.info("*************Home Page title test is failed **********************")
            assert False

    def test_Login(self,setup):

        #self.logger.info("****************Verifying Login Test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            #self.logger.info("***********Login Test is passed**********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login.png")
            self.driver.close()
            #self.logger.error("***********Login Test is failed**********************")
            assert False

