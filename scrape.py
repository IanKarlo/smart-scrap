import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def local_scrape(url: str, chrome_driver_path: str) -> str:
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        driver.get(url)
        print('Scraping successful...')
        html = driver.page_source
        time.sleep(10)
        return html
    finally:
        driver.quit()

def remote_scrape(url, driver_path: str) -> str:
    # Implement a remote scraper using Selenium and brightdata
    return "Remote scraper implementation not implemented"

def extract_body_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    body = soup.body
    if body:
        return str(body)
    return ""

def clean_body_content(body):
    soup = BeautifulSoup(body, 'html.parser')

    for script_or_style in soup(['script', 'style']):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    return cleaned_content

def scrape_website(url: str, driver_path: str, type='local'):
    scrape_method = local_scrape if type == 'local' else remote_scrape

    html = scrape_method(url, driver_path)
    body = extract_body_content(html)
    cleaned_body = clean_body_content(body)

    return cleaned_body