import time

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    #logger = logGen.custom_logger()

    def test_Login_ddt(self,setup):
        # self.logger.info("****************Test_002_DDT_Login*************************")
        #self.logger.info("****************Verifying Login DDT Test*************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows= XLUtils.getRowCount(self.path,"sheet1")
        print("No of Rows in Excel ", self.rows)

        list_status = []

        for r in range(2,self.row+1):
            self.user = XLUtils.readData(self.path,"sheet1",r,1)
            self.password = XLUtils.readData(self.path, "sheet1", r, 2)
            self.exp = XLUtils.readData(self.path, "sheet1", r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    #self.logger.info("****passed****")
                    print("****Passed****")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    #self.logger.info("****Failed****")
                    print("****Failed****")
                    self.lp.clicklogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    #self.logger.info("****Failed****")
                    print("****Failed****")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    #self.logger.info("****Passed****")
                    print("****Passed****")
                    list_status.append("Passed")

        if "Fail" not in list_status:
            #self.logger.info("****Login DDT Test passed****")
            print("****Login DDT Test passed****")
            self.driver.close()
            assert True
        else:
            # self.logger.info("****Login DDT Test failed****")
            print("****Login DDT Test failed****")
            self.driver.close()
            assert False
        print("****End of the Login DDT Test ****")
        #self.logger.info("****End of the Login DDT Tes****")
        print("****************Test_002_DDT_Login*************************")
        #self.logger.info("****************Test_002_DDT_Login*************************")














