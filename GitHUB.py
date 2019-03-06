import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class  Webdriverpage(unittest.TestCase):
# create a new chrome session
    def setUp(self):
        self.driver = webdriver.Chrome("C:\\javapackage\\chromedriver_win32 (1)\\chromedriver.exe")

    def test_githup_signin_page(self):
        driver = self.driver
        driver.get("https://github.com/")

        #driver.save_screenshot("C:\\Users\\admin\\AppData\\Local\\Temp\\Temp1_chromedriver_win32.zip\\haiamazon.png")
        driver.maximize_window()
        a= driver.find_element_by_link_text("Sign in").send_keys(Keys.ENTER)
        login = driver.find_element_by_id('login_field')
        login.send_keys("NithyaBS")
        pwd = driver.find_element_by_id('password')
        pwd.send_keys("Mgtech@123")
        pwd.send_keys(Keys.ENTER)
        driver.implicitly_wait(15)
        strproject=driver.find_element_by_link_text('Start a project').click()


        try:
    #Create a new repository
            repname = driver.find_element_by_id('repository_name')
            repname.send_keys("Github")
            desc = driver.find_element_by_id('repository_description')
            desc.send_keys("Demo1")
            driver.find_element_by_id('repository_auto_init').click()

            #create repository
            element = driver.find_element_by_xpath('//*[@id="new_repository"]/div[3]/button')
            element.click()
            driver.implicitly_wait(15)

            #upload file
            upload = driver.find_element_by_link_text("Upload files")
            upload.click()

            #uploade the file in desktop
            uploadfile = "C:\\Users\\admin\\Desktop\\html5\\loginpage.html"
            driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[2]/form[2]/file-attachment/p/input').send_keys(uploadfile)
            driver.implicitly_wait(5)
            commit = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/form/button')
            commit.click()

        except NoSuchElementException:
                   print("Failed")
                   raise Exception(NoSuchElementException)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()