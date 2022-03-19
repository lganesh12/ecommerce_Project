from selenium.webdriver.common.by import By


class LoginPage:
    textbox_userName_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_link_text = "logout"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element(By.ID, self.textbox_userName_id).clear()
        self.driver.find_element(By.ID,self.textbox_userName_id).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_link_text).click()