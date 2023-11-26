from django.test import LiveServerTestCase
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("window-size=1440,1080")
#chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("force-device-scale-factor=0.5")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--start-fullscreen")

driver = webdriver.Chrome(options=chrome_options)
# driver.set_window_size(1080, 1440)

class Teste(LiveServerTestCase):
    def test_001(self):
        driver.get("https://www.google.com.br/?hl=pt-BR")
        self.assertTrue(True)
