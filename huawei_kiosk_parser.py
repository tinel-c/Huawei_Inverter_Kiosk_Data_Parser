from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import gmtime, strftime
import time
import datetime
import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.connect("192.168.2.4", 1883, 60)


#Get data from the webpage

#--| Setup
options = Options()
#options.add_argument("--headless")
#options.add_argument("--window-size=1980,1020")
browser = webdriver.Chrome(options=options)
#--| Parse or automation
url = "https://uni003eu5.fusionsolar.huawei.com/pvmswebsite/nologin/assets/build/cloud.html#/kiosk?kk=8DkvnsA41e3fbzMJwPFe1OFKpcwE9Aqr"
browser.get(url)
time.sleep(3)
# Use BeautifulSoup
soup = BeautifulSoup(browser.page_source, 'lxml')
print(soup)
title = soup.find_all('p', class_="nco-kiosk-overview-data")

print(title[0].text)
print(title[1].text)
print(title[2].text)
print(title[3].text)
print(title[4].text)
now = datetime.datetime.now()
print(now)

mqttc.publish("Huawei/real-power", title[0].text[:-2])
mqttc.publish("Huawei/real-power-unit", title[0].text[-2:])
mqttc.publish("Huawei/yield-today", title[1].text[:-3])
mqttc.publish("Huawei/yield-today-unit", title[1].text[-3:])
mqttc.publish("Huawei/yield-this-month", title[2].text[:-3])
mqttc.publish("Huawei/yield-this-month-unit", title[2].text[-3:])
mqttc.publish("Huawei/yield-this-year", title[3].text[:-3])
mqttc.publish("Huawei/yield-this-year-unit", title[3].text[-3:])
mqttc.publish("Huawei/total-yield", title[4].text[:-3])
mqttc.publish("Huawei/total-yield-unit", title[4].text[-3:])
mqttc.publish("Huawei/report-time", str(now))



# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#mqttc.loop_forever()
