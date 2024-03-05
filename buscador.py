# scraper that gets data from the web
# throws ready to machine in endpoint?
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_data(driver, url):
    driver.get(url)
    time.sleep(2)

def main():
    driver = init_driver()
    urls = [
    'https://www.olx.com.br/imoveis/estado-rj/rio-de-janeiro-e-regiao/niteroi'
    ]
    for url in urls:
        scrape_data(driver, url)
    driver.quit()

if __name__ == '__main__':
    main()
