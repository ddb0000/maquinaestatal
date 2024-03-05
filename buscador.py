from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_data(driver, url):
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        listings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'section[data-ds-component="DS-AdCard"]')))
        for listing in listings:
            try:
                title = listing.find_element(By.CSS_SELECTOR, 'h2[class*="olx-ad-card__title"]').text
                price = listing.find_element(By.CSS_SELECTOR, 'h3[class*="olx-ad-card__price"]').text
                print(f"{title} - {price}")
            except Exception as e:
                print(f"Error in listing extraction: {e}")
    except Exception as e:
        print(f"An error occurred during scraping: {e}")

def main():
    driver = init_driver(headless=False)
    url = 'https://www.olx.com.br/imoveis/estado-rj/rio-de-janeiro-e-regiao/niteroi?sf=1'
    try:
        scrape_data(driver, url)
    except KeyboardInterrupt:
        print("Script interrupted by user.")
    finally:
        driver.quit()
        print("Driver closed.")

if __name__ == '__main__':
    main()
