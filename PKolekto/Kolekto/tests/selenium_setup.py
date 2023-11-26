from selenium import webdriver
import chromedriver_autoinstaller



driver = None
chrome_options = webdriver.ChromeOptions()

options = [
    "--ignore-certificate-errors",
    "--window-size=1920,1200",
    "--headless",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]

for option in options:
    chrome_options.add_argument(option)

def setup_selenium():
    global driver
    chromedriver_autoinstaller.install()
    if driver is None:
        driver = webdriver.Chrome(options=chrome_options)
    return driver

def finalizar_selenium():
    global driver
    if driver:
        driver.quit()
        driver = None

    return driver
