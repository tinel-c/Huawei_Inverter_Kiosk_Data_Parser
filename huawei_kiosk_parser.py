#! /usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import gmtime, strftime
import time
import datetime
import paho.mqtt.client as mqtt
from selenium.webdriver.chrome.service import Service
import paho.mqtt.publish as publish

def main():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--remote-debugging-port=9222")
    options.headless = True
    browser = webdriver.Chrome(options=options)


    #--| Parse or automation
    url = "https://uni003eu5.fusionsolar.huawei.com/pvmswebsite/nologin/assets/build/cloud.html#/kiosk?kk=8DkvnsA41e3fbzMJwPFe1OFKpcwE9Aqr"
    browser.get(url)
    time.sleep(3)
    # Use BeautifulSoup
    soup = BeautifulSoup(browser.page_source, 'lxml')
    title = soup.find_all('p', class_="nco-kiosk-overview-data")

    print(title[0].text)
    print(title[1].text)
    print(title[2].text)
    print(title[3].text)
    print(title[4].text)
    now = datetime.datetime.now()
    print(now)

    #Publish to mqtt

    publish.single("Huawei/real-power", payload=title[0].text[:-2],hostname="192.168.2.4",port=1883, client_id="huawei_parser")
    publish.single("Huawei/real-power-unit", payload=title[0].text[-2:],hostname="192.168.2.4",port=1883, client_id="huawei_parser")

    publish.single("Huawei/yield-today", payload=title[1].text[:-3],hostname="192.168.2.4",port=1883, client_id="huawei_parser")
    publish.single("Huawei/yield-today-unit", payload=title[1].text[-3:],hostname="192.168.2.4",port=1883, client_id="huawei_parser")

    publish.single("Huawei/yield-this-month", payload=title[2].text[:-3],hostname="192.168.2.4",port=1883, client_id="huawei_parser")
    publish.single("Huawei/yield-this-month-unit", payload=title[2].text[-3:],hostname="192.168.2.4",port=1883, client_id="huawei_parser")

    publish.single("Huawei/yield-this-year", payload=title[3].text[:-3],hostname="192.168.2.4",port=1883, client_id="huawei_parser")
    publish.single("Huawei/yield-this-year-unit", payload=title[3].text[-3:],hostname="192.168.2.4",port=1883, client_id="huawei_parser")

    publish.single("Huawei/total-yield", payload=title[4].text[:-3],hostname="192.168.2.4",port=1883, client_id="huawei_parser")
    publish.single("Huawei/total-yield-unit", payload=title[4].text[-3:],hostname="192.168.2.4",port=1883, client_id="huawei_parser")

    publish.single("Huawei/report-time", payload=str(now),hostname="192.168.2.4",port=1883, client_id="huawei_parser")

if __name__ == '__main__':
    main()