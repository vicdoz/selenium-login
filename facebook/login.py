from driver.driver import Driver
from config.config import Config
from selenium.webdriver.common.keys import Keys
import time


class Facebook:
    config = None
    driver = None

    def __init__(self):
        print("Init driver....")
        self.config = Config()
        self.driver = Driver().driver
        self.wait_seconds_logged = 20


    def login(self):
        try:
            print("Search elements into page....")
            self.driver.get(self.config.get_key('fb', 'url'))
            elem = self.driver.find_element_by_id('email')
            elem.send_keys(self.config.get_key('fb', 'user'))
            elem = self.driver.find_element_by_id('pass')
            elem.send_keys(self.config.get_key('fb', 'password'))
            elem.send_keys(Keys.RETURN)
            print("Logged!.Waiting %s s " % self.wait_seconds_logged)
            time.sleep(self.wait_seconds_logged)
            print("Finished")
        except Exception as ex:
            print("Can't login into Facebook")
            print(ex.__str__())
        finally:
            self.driver.close()
