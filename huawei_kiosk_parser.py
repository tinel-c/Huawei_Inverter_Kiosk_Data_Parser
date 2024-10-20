# import necessary tools from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up chrome driver
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)

# navigate to the target webpage
driver.get("https://uni003eu5.fusionsolar.huawei.com/pvmswebsite/nologin/assets/build/cloud.html#/kiosk?kk=8DkvnsA41e3fbzMJwPFe1OFKpcwE9Aqr")

# wait for the product grid to load
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CLASS_NAME, "echarts-for-react")
    )
)

# print the complete HTML after JavaScript execution
print(driver.page_source)

# close the browser
driver.quit()
