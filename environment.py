from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def before_scenario(context, scenario):
    print('Before scenario')

    if 'UI' in scenario.name:
        # create a new Firefox session
        context.driver = webdriver.Safari()
        context.driver.implicitly_wait(30)
        # driver.maximize_window()

        # Navigate to the application home page
        context.driver.get("https://www.eurosport.co.uk")
    else:
        print('Did not start chromedriver')

    context.before = 'done'


def after_scenario(context, scenario):
    print('After scenario')
    if 'UI' in scenario.name:
        context.driver.close()
    else:
        print('Did not stop chromedriver')
    context.after = 'done'
