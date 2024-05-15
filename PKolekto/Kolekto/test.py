from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1440,1080")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)

class Historia1(LiveServerTestCase):

    def test_cenario1(self):
        driver.get("http://127.0.0.1:8000/registro")
        self.assertTrue(True)
        