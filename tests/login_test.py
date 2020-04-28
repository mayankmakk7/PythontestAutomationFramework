import time
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.Homepage import Homepage
from utils import utils as ut
import allure
import moment


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver=self.driver
        driver.get(ut.url)
        login=LoginPage(driver)
        login.enter_username(ut.username)
        login.enter_password(ut.password)
        login.click_login()
        time.sleep(5)
    def test_logout(self):
        try:
            driver = self.driver
            homepage=Homepage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x=driver.title
            assert x=='abc'
        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currtime=moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName=ut.whoami()
            screenShotName=testName+"_"+currtime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenShotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("/Users/mayank/PycharmProjects/testAutomationFramework/Screenshots/"+screenShotName+".png")
            raise
        except:
            print("Some exception occurred")
        else:
            print("No exceptions occurred")
        finally:
            print("This block will (lw(ys execute | Close DB")










