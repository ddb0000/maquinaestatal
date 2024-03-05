from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')  # Bypass OS security model, required for Docker
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    driver = webdriver.Chrome(options=options)
    return driver

def scrape_data(driver, url):
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    # Wait for the specific element to ensure the page has loaded
    listings = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'section[data-ds-component="DS-AdCard"]')))
    for listing in listings:
        # Get the title of the listing
        try:
            title = listing.find_element(By.CSS_SELECTOR, 'h2[class*="olx-ad-card__title"]').text
        except Exception as e:
            title = "No Title"
            print(f"Error getting title: {e}")
        
        # Get the price of the listing
        try:
            price = listing.find_element(By.CSS_SELECTOR, 'h3[class*="olx-ad-card__price"]').text
        except Exception as e:
            price = "No Price"
            print(f"Error getting price: {e}")
        
        print(f"{title} - {price}")

def main():
    driver = init_driver(headless=False)  # Set headless=False to see what the browser is doing
    url = 'https://www.olx.com.br/imoveis/estado-rj/rio-de-janeiro-e-regiao/niteroi'
    scrape_data(driver, url)
    driver.quit()

if __name__ == '__main__':
    main()
