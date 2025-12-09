from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urljoin

BASE = "https://www.goafricaonline.com/bj/annuaire"



def init_driver():
    try:
        options = Options()
        options.add_argument("-headless=new")
        options.add_argument("-no-sandbox")
        options.add_argument("-disable-gpu")
        options.add_argument("-window-size=1920,1200")
        options.add_argument("user-agent=ScraperBot/1.0 (+https://yourdomain.example; contact: ton-email@example.com)")
        driver = webdriver.Chrome(options=options)
        return driver
    except Exception as e:
        print(f"Error on driver initialization: {e}")


def get_cat():
    try:
        print("Getting categories")
        cat_cards = driver.find_elements(By.CLASS_NAME, "stretched-link")    
        cat_cards = cat_cards[:len(cat_cards)-2]
        cat_links = {}

        for cat in cat_cards:
            cat_links[cat.text] = cat.get_attribute('href')
            
        return cat_links
    except Exception as e:
        print(f"Error on category fetching : {e}")

def get_subcat(categories):
    try:
        print("Getting sub-categories")
        subcat_links = {}
        for link in categories.values():
            driver.get(link)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "stretched-link.text-center")))
            subcat_cards = driver.find_elements(By.CLASS_NAME, "stretched-link.text-center")

            for subcat in subcat_cards:
                subcat_links[subcat.text] = subcat.get_attribute('href')
                
        return subcat_links
    except Exception as e:
        print(f"Error on subcat fetching: {e}")


def get_entreprises(subcategories):
    try: 
        print("Getting entreprises")
        entreprises = []
        for link in subcategories.values():
            driver.get(link)
            print(f"{link} : {type(link)}")
            driver.get(link)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "stretched-link")))
            entreprises_cards = driver.find_elements(By.TAG_NAME, "article")
            entreprises = []

            for entreprise in entreprises_cards:
                
                master = entreprise.find_element(By.XPATH,".//div[@class = 'w-full']")               
                entreprises.append(
                    {
                        "name": entreprise.find_element(By.TAG_NAME, 'h2').text if entreprise.find_element(By.TAG_NAME, 'h2') else None,
                        "category": entreprise.find_element(By.CLASS_NAME, 'text-brand-blue').text if entreprise.find_element(By.CLASS_NAME, 'text-brand-blue') else None,
                        "address": entreprise.find_element(By.TAG_NAME, 'address').text if entreprise.find_element(By.TAG_NAME, 'address') else None,
                        "tel": entreprise.find_element(By.XPATH,".//i[contains(@class, 'tnp-smartphone-2')]//following-sibling::a").text.replace("Gsm: ", "").replace("(", "").replace(")", "").replace(" ", "") if entreprise.find_element(By.XPATH,".//i[contains(@class, 'tnp-smartphone-2')]//following-sibling::a") else None,
                        "description" : master.find_element(By.XPATH,"./child::div[4]").text if master.find_element(By.XPATH,"./child::div[4]") else None,          
                    }
                )
        return entreprises
    except Exception as e:
        print(f"Error on entreprises fetching: {e}")

def save_to_csv(entreprises):
    try:
        with open("goafrica_entreprises.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[entreprises[0].keys()])
            writer.writeheader()
            for e in entreprises:
                writer.writerow({
                    "name": e["name"],
                    "category": e["category"],
                    "address": e["address"],
                    "tel": e["tel"],
                    "description": e["description"],
                })
    except Exception as e:
        print(f"Error on csv saving: {e}")


try:

    #driver initialization
    driver = init_driver()
    print("Getting page")
    driver.get(BASE)
    wait = WebDriverWait(driver, 5)


    #categories fetching
    categories = get_cat()

    #subcategories fetching
    subcategories = get_subcat(categories)

    #entreprises fetching
    entreprises = get_entreprises(subcategories)


    #entreprises saving
    save_to_csv(entreprises)

except Exception as e:
    print(f"Error: {e}")

# for category, link in categories.items():
#     print(f"{category} : {link}")

# for subcategory, link in subcategories.items():
#     print(f"{subcategory} : {link}")


    
# links = ["https://www.goafricaonline.com/bj/annuaire/transports-logistiques"]


# for link in links:
#     print(f"{link} : {type(link)}")
#     driver.get(link)
#     wait = WebDriverWait(driver, 5)
#     wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "stretched-link")))
#     entreprises_cards = driver.find_elements(By.TAG_NAME, "article")
#     entreprises = []

#     for entreprise in entreprises_cards:
        
#         master = entreprise.find_element(By.XPATH,".//div[@class = 'w-full']")               
#         entreprises.append(
#             {
#                 "name": entreprise.find_element(By.TAG_NAME, 'h2').text if entreprise.find_element(By.TAG_NAME, 'h2') else None,
#                 "category": entreprise.find_element(By.CLASS_NAME, 'text-brand-blue').text if entreprise.find_element(By.CLASS_NAME, 'text-brand-blue') else None,
#                 "address": entreprise.find_element(By.TAG_NAME, 'address').text if entreprise.find_element(By.TAG_NAME, 'address') else None,
#                 "tel": entreprise.find_element(By.XPATH,".//i[contains(@class, 'tnp-smartphone-2')]//following-sibling::a").text.replace("Gsm: ", "").replace("(", "").replace(")", "").replace(" ", "") if entreprise.find_element(By.XPATH,".//i[contains(@class, 'tnp-smartphone-2')]//following-sibling::a").text else None,
#                 "description" : master.find_element(By.XPATH,"./child::div[4]").text if master.find_element(By.XPATH,"./child::div[4]").text else None,          
#             }
#         )



# nb_pages = int(len(driver.find_elements(By.CLASS_NAME, "button.pagination-btn"))) - 2
# cards = []
# entreprises = []

# for page in range(nb_pages):
#     print(f"Scraping page {page+1}/{nb_pages}...")

#     # attendre les cartes de la page
#     wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "company-card")))
#     cards = driver.find_elements(By.CLASS_NAME, "company-card")

#     for card in cards:
#         name = card.find_element(By.CLASS_NAME, "name").text.strip()
#         nature = card.find_element(By.CLASS_NAME, "meta-tag").text.strip()

#         chip_elements = card.find_elements(By.CLASS_NAME, "chip")
#         tags = [chip.text.strip() for chip in chip_elements]

#         entreprises.append({
#             "name": name,
#             "nature": nature,
#             "tags": tags
#         })

#     # bouton "next"
#     next_btn = driver.find_elements(By.CLASS_NAME, "pagination-btn")[-1]
#     driver.execute_script("arguments[0].click();", next_btn)
#     time.sleep(3)

driver.quit()

# with open("ahilido_entreprises.csv", "w", newline="", encoding="utf-8") as f:
#     writer = csv.DictWriter(f, fieldnames=["name", "nature", "tags"])
#     writer.writeheader()
#     for e in entreprises:
#         writer.writerow({
#             "name": e["name"],
#             "nature": e["nature"],
#             "tags": ", ".join(e["tags"])
#         })

# print("Fini → fichier créé : ahilido_entreprises.csv")
