import json
from collections import OrderedDict

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

url = "https://onepieceex.net/mangas/leitor/"
options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

chapter_start = 1
chapter_end = 1103

for chapter in range(chapter_start, chapter_end + 1):
    print(f"Chapter {chapter}")

    driver.get(url + str(chapter))

    element_present = EC.presence_of_element_located((By.CLASS_NAME, 'paginamanga'))
    WebDriverWait(driver, 600).until(element_present)

    pages = []
    while True:
        print(f"Page {len(pages) + 1}")
        page = driver.find_element(By.CLASS_NAME, 'paginamanga')
        src = page.get_attribute('src')
        if len(pages) != 0 and src == pages[-1]:
            break
        pages.append(src)
        page.click()

    with open("image_urls.json", "r") as f:
        data = json.load(f)
    data[str(chapter)] = pages
    sorted_data = OrderedDict(sorted(data.items(), key=lambda x: int(x[0])))
    with open("image_urls.json", "w") as f:
        f.write(json.dumps(sorted_data, sort_keys=False, indent=4, separators=(',', ': ')))

    print("==============")

driver.close()