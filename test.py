import sys
import json
import os    
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import math
import urllib
import urllib.request

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

driver.get('https://student.emeritus.org/courses/4208/pages/module-introduction-introduction-to-pandas-10-28?module_item_id=829317')
time.sleep(1)
playBtnPath = '/html/body/div[1]/div[2]/a'
driverIframes = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/p[2]/iframe')
driverIframes = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/p[6]/iframe')
driverIframes = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/p[8]/iframe')
for c in range(0, len(driverIframes)):
    driver.switch_to.frame(driverIframes[c])
    time.sleep(1)
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="kplayer_ifp"]'))
    driver.find_element(By.XPATH, playBtnPath).click()
    time.sleep(5)
    test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
    for item in test:
        if "https://cfvod.kaltura.com/scf/enc/hls/p" in item["name"]:
            print(item["name"])
            originLink = '' + str(item['name'])
            videoLink = originLink.replace('scf/enc/hls', 'pd')
            # driver.execute_script("window.open('" + videoLink + "', 'new window')")
            # driver.switch_to.window( driver.window_handles[1])
            time.sleep(1)
            # driver.get(videoLink)
            time.sleep(1)
            # video = driver.find_element(By.TAG_NAME, '/html/body/video/source')
            # video_url = video.get_property('src')
            # print(video_url)
            urllib.request.urlretrieve(videoLink, 'videoname.mp4')
            driver.execute_script("window.close()")
        #   filename = max([download_folder + "\\" + f for f in os.listdir(download_folder)],key=os.path.getctime)
        #   shutil.move(filename,os.path.join(download_folder, pdfName))
    time.sleep(500)
driver.close()    


# module2 = driver.find_element(By.XPATH, module2Path)

# lists = module2.find_elements(By.TAG_NAME, 'li')
# linkPath = '/div/div[1]/div[1]/span/a'
# for c in range(0, len(lists)):
#   if lists[c].find_elements(By.TAG_NAME, 'a'):
#     link = lists[c].find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
#     print(link)
# title = driver.find_element(By.XPATH, titlePath).click()
# time.sleep(10)
# driver.execute_script('window.print();')
# # title = driver.find_element(By.XPATH, titlePath).get_attribute('innerHTML')
# # print(title)
# playButtonPath = '/html/body/div[1]/div[2]/a'

# test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
# for item in test:
#   if "https://cfvod.kaltura.com/scf/enc/hls/p" in item["name"]:
#     print(item["name"])

# test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
# for item in test:
#   data = json.loads(item)
#   if item["name"]:
#     print(item["name"])
#   if(item.name == "https://cfvod.kaltura.com/scf/enc/hls/p") print(item.name)
# driver.find_element(By.XPATH, passwordButtonPath).send_keys(u'\ue007')
# driver.find_element(By.XPATH, passwordPath).send_keys(password)
