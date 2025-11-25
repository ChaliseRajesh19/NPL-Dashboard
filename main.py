from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# ----------------------------
# 1️⃣ Setup Selenium
# ----------------------------
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # keeps browser open
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ----------------------------
# 2️⃣ Open NPL Records Page
# ----------------------------
url = "https://www.espncricinfo.com/records/trophy/nepal-premier-league-1078"
driver.get(url)
time.sleep(5)  # wait for page to load fully

# ----------------------------
# 3️⃣ Scrape all tables
# ----------------------------
soup = BeautifulSoup(driver.page_source, "lxml")

# Create folder to save CSVs
if not os.path.exists("npl_overall_stats"):
    os.makedirs("npl_overall_stats")

# Each table is inside <div class="ds-w-full ds-table ds-table-md ds-table-auto ci-stats-table">
tables = soup.find_all("table")

for idx, table in enumerate(tables):
    # Get headers
    headers = [th.text.strip() for th in table.find_all("th")]

    # Get rows
    rows = []
    for tr in table.find_all("tr")[1:]:
        cols = [td.text.strip() for td in tr.find_all("td")]
        if cols:
            rows.append(cols)

    # Save to DataFrame
    df = pd.DataFrame(rows, columns=headers)
    
    # Save as CSV
    csv_name = f"npl_overall_stats/table_{idx+1}.csv"
    df.to_csv(csv_name, index=False)
    print(f"Saved table {idx+1} as {csv_name}")

driver.quit()
