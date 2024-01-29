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

tensor = driver.find_element(By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
tensor.click()
wh = driver.window_handles

driver.switch_to.window(wh[-1])
element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/div/div/div[1]/div/div[5]/div/div/div[1]/div/p[1]'))
        )

about = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
driver.get(about.get_attribute("href"))

gallery = driver.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')
if (all(i.get_attribute("height") == gallery[0].get_attribute("height") for i in gallery) and all(i.get_attribute("width") == gallery[0].get_attribute("width") for i in gallery)):
    print("It's okay")
print("?")
