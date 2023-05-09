import sys
import json
import os    
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import math

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import csv
import time 
from selenium.webdriver.common.action_chains import ActionChains

# options = Options()
# options.add_argument("start-maximized")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

download_folder = "C:\\Users\\Samet Gjonaj\\Downloads"
save_folder = "C:\\Users\\Samet Gjonaj\\Downloads\\New folder"

# it's for creating pdf
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        # "download.default_directory": "F:\Online Content\Module 2",
    }
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
options.add_experimental_option('prefs', prefs)
options.add_argument('--kiosk-printing')
# end of creating pdf setting.

# network
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
# network

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options, desired_capabilities=desired_capabilities)

mailPath = '//*[@id="student_email"]'
mailSubmitPath = '/html/body/main/div/div/div/form/input[2]'
passwordPath = '//*[@id="user_password"]'
passwordSubmitPath = '//*[@id="new_user"]/input[4]'

driver.get('https://student.emeritus.org/courses/4208/modules')

time.sleep(1)
driver.find_element(By.XPATH, mailPath).send_keys('rajatnathan@icloud.com')
time.sleep(1)
driver.find_element(By.XPATH, mailSubmitPath).click()

time.sleep(1)
driver.find_element(By.XPATH, passwordPath).send_keys('deggu0-hiskaz-cebJed')
time.sleep(1)
driver.find_element(By.XPATH, passwordSubmitPath).click()
time.sleep(50)

# driver.execute_script('window.print();')
# time.sleep(2)
# filename = max([download_folder + "\\" + f for f in os.listdir(download_folder)],key=os.path.getctime)
# shutil.move(filename,os.path.join(download_folder,r"newPDFName.pdf"))

with open('module 20.csv', mode='r') as file:
    reader = csv.reader(file)
    pdfId = 0
    for row in reader:
      link = row[2]
      pdfIdString = str(math.floor(pdfId / 100)) + str(math.floor(pdfId / 10) % 10)  + str(pdfId % 10)
      pdfName = row[0] + '_' + pdfIdString + '_' + row[1] + '.pdf'
      pdfId = pdfId + 1
    #   for i in range(0, len(pdfName)):
    #      if(pdfName[i] == ':'):
    #         pdfName[i] = '-'
      driver.get(link)
      time.sleep(1)
      driver.execute_script('window.print();')
      time.sleep(2)
      filename = max([download_folder + "\\" + f for f in os.listdir(download_folder)],key=os.path.getctime)
      shutil.move(filename,os.path.join(download_folder, pdfName))
driver.close()    
