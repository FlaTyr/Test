import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


url = "https://sbis.ru/contacts"
options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=options)

driver.get(url)

region = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
old_data = [driver.current_url, region.text]
partners = [i.get_attribute("item-key") for i in driver.find_elements(By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div')]
region.click()
element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span'))
        )
driver.find_element(By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span').click()

time.sleep(1)
if(old_data != [driver.current_url, driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span').text] and partners != [i.get_attribute("item-key") for i in driver.find_elements(By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div')]):
    print("It's okay") 
print("?")