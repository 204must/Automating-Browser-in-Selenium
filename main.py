from selenium import webdriver
from selenium.webdriver.chrome import Chromedriver
def open_browser(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    return driver

if __name__ == "__main__":
    driver = open_browser("https://www.google.com")
    driver.quit()
