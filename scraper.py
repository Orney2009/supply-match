# scrape_ahilido_selenium.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

BASE = "https://www.ahilido.bj"
LIST_URL = urljoin(BASE, "/entreprises")

options = Options()
options.add_argument("-headless=new")
options.add_argument("-no-sandbox")
options.add_argument("-disable-gpu")
options.add_argument("-window-size=1920,1200")
options.add_argument("user-agent=ScraperBot/1.0 (+https://yourdomain.example; contact: ton-email@example.com)")

driver = webdriver.Chrome(options=options)  # Assure-toi que chromedriver est installé et dans PATH
driver.get(LIST_URL)
wait = WebDriverWait(driver, 20)
time.sleep(10)



nb_pages = int(len(driver.find_elements(By.CLASS_NAME, "button.pagination-btn"))) - 2
cards = []
entreprises = []

for page in range(nb_pages):
    print(f"Scraping page {page+1}/{nb_pages}...")

    # attendre les cartes de la page
    wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "company-card")))
    cards = driver.find_elements(By.CLASS_NAME, "company-card")

    for card in cards:
        name = card.find_element(By.CLASS_NAME, "name").text.strip()
        nature = card.find_element(By.CLASS_NAME, "meta-tag").text.strip()

        chip_elements = card.find_elements(By.CLASS_NAME, "chip")
        tags = [chip.text.strip() for chip in chip_elements]

        entreprises.append({
            "name": name,
            "nature": nature,
            "tags": tags
        })

    # bouton "next"
    next_btn = driver.find_elements(By.CLASS_NAME, "pagination-btn")[-1]
    driver.execute_script("arguments[0].click();", next_btn)
    time.sleep(3)

driver.quit()

with open("ahilido_entreprises.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "nature", "tags"])
    writer.writeheader()
    for e in entreprises:
        writer.writerow({
            "name": e["name"],
            "nature": e["nature"],
            "tags": ", ".join(e["tags"])
        })

print("Fini → fichier créé : ahilido_entreprises.csv")
