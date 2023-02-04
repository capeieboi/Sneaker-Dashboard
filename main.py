from selenium import webdriver
import time
from selenium import webdriver
import webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")
#driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
class SnkrsBot:

    def __init__(self, sneaker_url):
        self.sneaker_url =  sneaker_url
        self.driver = webdriver.Chrome(options=options, service_log_path='selenium.log') 
    
    def get_price(self):
        self.driver.get(self.sneaker_url)
        price = self.driver.find_element(by=By.XPATH, value='//div[@data-qa="price"]')
        return float(price.get_attribute('innerHTML').strip('$'))
    
    def get_sizes_available(self):
        self.driver.get(self.sneaker_url)
        sizes_avail = self.driver.find_element(by=By.XPATH, value='//div[@data-qa="size-available"]')
        print(sizes_avail)


def main():
    url = 'https://www.nike.com/launch/t/air-force-1-low-x-undefeated-mens-shoes'
    bot = SnkrsBot(url)

    last_price = None
    while 1:
        price = bot.get_price()
        bot.get_sizes_available()
        if last_price:
            if price < last_price:
                print(f"Price dropped: {last_price - price}")
            elif price > last_price:
                print(f"Price rose: {price - last_price}")
            else:
                print(f"Price stayed: {price}")
        last_price = price
        time.sleep(5)

if __name__ == "__main__":
    main()