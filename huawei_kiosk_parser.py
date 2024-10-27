from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import gmtime, strftime
#from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import paho.mqtt.client as mqtt
from selenium.webdriver.chrome.service import Service
import paho.mqtt.publish as publish


# The callback for when the client receives a CONNACK response from the server.
#def on_connect(client, userdata, flags, reason_code, properties):
#    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
#    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
#def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))

#mqttc = mqtt.Client()
#mqttc.on_connect = on_connect
#mqttc.on_message = on_message

#mqttc.connect("192.168.2.4", 1883, 60)


#Get data from the webpage

#--| Setup
#service = Service(executable_path=r'/usr/bin/chromedriver')
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument("--remote-debugging-port=9222")
options.headless = True
#options.headless = True
#options.add_argument("--headless")
#options.add_argument("--window-size=1980,1020")
#browser = webdriver.Chrome(service=service, options=options)
browser = webdriver.Chrome(options=options)
#browser = webdriver.Chrome(service=ChromeDriverManager().install(),options=options)
#--| Parse or automation
url = "https://uni003eu5.fusionsolar.huawei.com/pvmswebsite/nologin/assets/build/cloud.html#/kiosk?kk=8DkvnsA41e3fbzMJwPFe1OFKpcwE9Aqr"
browser.get(url)
time.sleep(3)
# Use BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')
#print(soup)
title = soup.find_all('p', class_="nco-kiosk-overview-data")

print(title[0].text)
print(title[1].text)
print(title[2].text)
print(title[3].text)
print(title[4].text)
now = datetime.datetime.now()
print(now)

#mqttc.publish("Huawei/real-power", title[0].text[:-2])
#mqttc.publish("Huawei/real-power-unit", title[0].text[-2:])
#mqttc.publish("Huawei/yield-today", title[1].text[:-3])
#mqttc.publish("Huawei/yield-today-unit", title[1].text[-3:])
#mqttc.publish("Huawei/yield-this-month", title[2].text[:-3])
#mqttc.publish("Huawei/yield-this-month-unit", title[2].text[-3:])
#mqttc.publish("Huawei/yield-this-year", title[3].text[:-3])
#mqttc.publish("Huawei/yield-this-year-unit", title[3].text[-3:])
#mqttc.publish("Huawei/total-yield", title[4].text[:-3])
#mqttc.publish("Huawei/total-yield-unit", title[4].text[-3:])
#mqttc.publish("Huawei/report-time", str(now))

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





# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#mqttc.loop_forever()

