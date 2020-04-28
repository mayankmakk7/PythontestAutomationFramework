#Constants
import inspect
url='https://opensource-demo.orangehrmlive.com/'
username='Admin'
password='admin123'


def whoami():
    return inspect.stack()[1][3]