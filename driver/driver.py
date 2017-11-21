from selenium import webdriver


class Driver:
    driver = None

    def __init__(self):
        self.driver = webdriver.Firefox()
