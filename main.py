from selenium import webdriver
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.common.by import By
class SnkrsBot:

    def __init__(self, sneaker_url):
        self.sneaker_url =  sneaker_url
        self.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    
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