import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome", help="Type in browser name e.g.chrome OR firefox")

@pytest.fixture(scope='class')
def test_setup(request):
    #global driver
    browser = request.config.getoption("--browser")
    if browser=='chrome':
        driver = webdriver.Chrome(executable_path='/Users/mayank/PycharmProjects/testAutomationFramework/drivers/chromedriver')
    elif browser=='firefox':
        driver=webdriver.Firefox()

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.close()
    driver.quit()
    print("done")