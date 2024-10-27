# Huawei_Inverter_Kiosk_Data_Parser
## Installation on ubuntu

Update the system
```
sudo apt update
```

Istall python
```
sudo apt install python3
```

Check that python is installed
```
python3 --version
```

Install chromium
```
sudo apt-get install chromium-browser
```
Install pip
```
sudo apt install python3-pip
```

Install python packages

```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
pip install selenium
pip install beautifulsoup4
pip install lxml
pip install paho-mqtt
pip install webdriver-manager
```

```
sudo apt install python3-selenium
sudo apt-get install python3-bs4
sudo apt install python3-paho-mqtt
```

Clone github respository
```
git clone https://github.com/tinel-c/Huawei_Inverter_Kiosk_Data_Parser.git
```

Get Chrome driver 

https://skolo.online/documents/webscrapping/#step-2-install-chromedriver

Test that the script is working


