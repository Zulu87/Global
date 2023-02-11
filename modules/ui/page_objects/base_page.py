import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service



class BasePage:
    PATH = 'C:\\Users\\Pavlo.Znak\\Global\\' 
    DRIVERNAME = 'chromedriver.exe'

    def __init__(self) -> None:
        self.driver = webdriver.Chrome (
            service = Service(BasePage.PATH + BasePage.DRIVERNAME)
            )
        
    def close(self):
        self.driver.close()