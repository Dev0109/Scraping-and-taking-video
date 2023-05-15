import sys
import json
import os    
import shutil
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import math

import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import csv
import time 
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import urllib.request

options = webdriver.ChromeOptions()
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

download_folder = "C:\\Users\\Samet Gjonaj\\Downloads"
save_folder = "C:\\Users\\Samet Gjonaj\\Downloads\\New folder"

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
time.sleep(5)
with open('Lesson Total.csv', mode='r') as file:
    reader = csv.reader(file)
    pdfId = 134
    for row in reader:
        link = row[2]
        print(link)
        videonameIndex = 0
        videoname = []
        video_name = ''
        exitVal = 0
        pdfIdString = str(math.floor(pdfId / 100)) + str(math.floor(pdfId / 10) % 10)  + str(pdfId % 10)
        pdfName = row[0] + '_' + pdfIdString + '_' + row[1] + '.pdf'
        pdfId = pdfId + 1
        driver.get(link)
        time.sleep(1)
        videoNameClass = 'kl_message_heading'
        playBtnPath = '/html/body/div[1]/div[2]/a'
        paragraphs = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/p')
        videoNames = driver.find_elements(By.TAG_NAME, 'strong')
        # videoNames = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/div/h4/strong')
        # print("videonames: ", videoNames)
        # print("videonames type: ", type(videoNames))
        nameIndex = 0
        videoNameString = []
        iframeindex = 0
        for l in range(0, len(paragraphs)):
            print("=========paragraphs==========")
            print("l==========>", l)
            time.sleep(1)
            print(paragraphs[l])
            if len(paragraphs[l].find_elements(By.TAG_NAME, 'iframe')):
                for x in range(0, len(videoNames)):
                    videoname_filter = videoNames[x].text
                    # print("videoname_filter", videoname_filter)
                    if ("There" not in videoname_filter and "Video " in videoname_filter and videoname_filter not in videoname):
                        videoname += [videoname_filter]
                        print("videoname", videoname)
                print(paragraphs[l].find_elements(By.TAG_NAME, 'iframe'))
                print("=========iframe==========")
                print(paragraphs[l])
                driverIframe = paragraphs[l].find_element(By.TAG_NAME, 'iframe')
                driver.switch_to.frame(driverIframe)
                time.sleep(2)
                if len(driver.find_elements(By.XPATH, '//*[@id="kplayer_ifp"]')):
                    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="kplayer_ifp"]'))
                    driver.find_element(By.XPATH, playBtnPath).click()
                    time.sleep(2)  
                    test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                    time.sleep(3)  
                    for item in test:
                        print("=========test==========")
                        if "https://cfvod.kaltura.com/scf/enc/hls/p" in item["name"] and exitVal == 0:
                            print("=========download==========")
                            print("x====>", videonameIndex)
                            video_name_before = '{}.mp4'
                            video__name = str(videoname[videonameIndex])
                            video_name = video_name_before.format(video__name)
                            print("video_name", video_name)
                            print("video_name type", type(video_name))
                            video_name = video_name.replace(':', '_')
                            videonameIndex = videonameIndex + 1
                            print(item["name"])
                            originLink = '' + str(item['name'])
                            videoLink = originLink.replace('scf/enc/hls', 'pd')
                            time.sleep(3)
                            response = requests.get(videoLink)   
                            with open(video_name, 'wb') as f:
                                f.write(response.content)
                            exitVal = exitVal + 1
                        if exitVal == 1:
                            print("exit================>")
                            break
                time.sleep(1)
            exitVal = 0
            print("continue================>")
            driver.switch_to.default_content()
driver.close()    