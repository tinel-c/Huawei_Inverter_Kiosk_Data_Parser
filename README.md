# Huawei_Inverter_Kiosk_Data_Parser
##
Read data from 
https://intl.fusionsolar.huawei.com/unisso/login.action?service=%2Funisess%2Fv1%2Fauth%3Fservice%3D%252Fnetecowebext%252Fhome%252Findex.html#/LOGIN

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

```
python3 huawei_kiosk_parser.py
```

To create a reccurent call create a crontab entry

https://www.geeksforgeeks.org/python-script-that-is-executed-every-5-minutes/

```
crontab -e
```

Insert the reccurence at which the script needs to be executed
```
*/1 * * * * /home/tinel/Huawei_Inverter_Kiosk_Data_Parser/huawei_kiosk_parser.py
```

Ensure that the virtual environment created is referenced inside the python file first line
```
echo $VIRTUAL_ENV
```

Make the script executable
```
chmod u+x /home/tinel/Huawei_Inverter_Kiosk_Data_Parser/huawei_kiosk_parser.py >/dev/null 2>&1
```

To check that crontab executed use the following command
```
grep CRON /var/log/syslog
```

