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

# driver.execute_script('window.print();')
# time.sleep(2)
# filename = max([download_folder + "\\" + f for f in os.listdir(download_folder)],key=os.path.getctime)
# shutil.move(filename,os.path.join(download_folder,r"newPDFName.pdf"))

with open('module 3.csv', mode='r') as file:
    reader = csv.reader(file)
    pdfId = 134
    videonameIndex = -1
    exitVal = 0
    for row in reader:
        link = row[2]
        print(link)
        pdfIdString = str(math.floor(pdfId / 100)) + str(math.floor(pdfId / 10) % 10)  + str(pdfId % 10)
        pdfName = row[0] + '_' + pdfIdString + '_' + row[1] + '.pdf'
        pdfId = pdfId + 1
        driver.get(link)
        time.sleep(1)
        videoNameClass = 'kl_message_heading'
        # videonamePath = '//*[@id="wiki_page_show"]/div/div[2]/h4/strong'
        playBtnPath = '/html/body/div[1]/div[2]/a'
        paragraphs = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/p')
        videoNames = driver.find_elements(By.XPATH, '//*[@id="wiki_page_show"]/div/div/h4/strong')
        print("videonames: ", videoNames)
        print("videonames type: ", type(videoNames))
        nameIndex = 0
        videoNameString = []
        iframeindex = 0
        # print("videoNames length")
        # print(len(videoNames))
        # print("paragraphs length")
        # print(len(paragraphs))
        # for x in range(0, len(videoNames)):
        #     print("=========videonames==========")
            # if videoNames[x].find_elements(By.TAG_NAME, 'h4'):
            #     print("title")
    #             print("nameIndex")
    #             print(nameIndex)
    #             videoNameString.append(videoNames[x].find_element(By.XPATH, '/h4/strong').get_attribute('innerHTML'))
    #             print("videoNameString: ", videoNameString)
    #       print("videoNameString length")
    #       print(len(videoNameString))
    #       print("paragraphs length")
    #       print(len(paragraphs))
        for l in range(0, len(paragraphs)):
            print("=========paragraphs==========")
            print("l==========>", l)
            time.sleep(1)
            if len(paragraphs[l].find_elements(By.TAG_NAME, 'iframe')):
                print(paragraphs[l].find_elements(By.TAG_NAME, 'iframe'))
                print("=========iframe==========")
                driverIframe = paragraphs[l].find_element(By.TAG_NAME, 'iframe')
                # thisVideoName = videoNameString[iframeindex]
                # iframeindex = iframeindex + 1
                # liststring = list(thisVideoName)
                # for c in range(0, len(liststring)):
                #     if liststring[c] == ':':
                #         liststring[c] = '-'
                # videoName = "".join(liststring)
                # print(videoName)
                driver.switch_to.frame(driverIframe)
                time.sleep(1)
                driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="kplayer_ifp"]'))
                driver.find_element(By.XPATH, playBtnPath).click()
                time.sleep(8)  
                test = driver.execute_script("var performance = window.performance || window.mozPerformance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;")
                for item in test:
                    print("=========test==========")
                    if "https://cfvod.kaltura.com/scf/enc/hls/p" in item["name"] and exitVal == 0:
                    # if "https://cfvod.kaltura.com/scf/enc/hls/p" in item["name"]:                                       
                        print("=========download==========")
                        videonameIndex = videonameIndex + 1
                        print("x====>", videonameIndex)
                        print(item["name"])
                        originLink = '' + str(item['name'])
                        videoLink = originLink.replace('scf/enc/hls', 'pd')     
                        videoname_before = '3_{}.mp4'
                        videoname = videoname_before.format(videonameIndex)
                        # driver.execute_script("window.open('" + videoLink + "', 'new window')")
                        # driver.switch_to.window( driver.window_handles[1])
                        # time.sleep(3)
                        # driver.get(videoLink)
                        time.sleep(3)
                        # video = driver.find_element(By.TAG_NAME, '/html/body/video/source')
                        # video_url = video.get_property('src')
                        # print(video_url)
                        # url = 'https://cfvod.kaltura.com/pd/p/2384071/sp/238407100/serveFlavor/entryId/1_2n8jk1nh/v/1/ev/7/flavorId/1_fntuxk95/name/a.mp4/seg-1-v1-a1.ts?Policy=eyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZnZvZC5rYWx0dXJhLmNvbS9zY2YvZW5jL2hscy9wLzIzODQwNzEvc3AvMjM4NDA3MTAwL3NlcnZlRmxhdm9yL2VudHJ5SWQvMV8ybjhqazFuaC92LzEvZXYvNy9mbGF2b3JJZC8xX2ZudHV4azk1L25hbWUvYS5tcDQvKiIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTY4MzcxNjg4OH19fV19&Signature=Spftq7GggyOll-FBm1jIe~J4BAQgRw8Bie66lz8OgTkukCAyAqoY7m3DcqVSxAvvqjEYbpJKYLSkcESITlglokvwxWt9Mz40drcyvqo3aX4Uk1sn-7--izNXiS31LBzHc6wr3Hu4sIt70bAjvRfHec3cLuCThAMtN9csB~XDUL5MyJUIKli8oDbB-cOL7avkZUzAGhnWmfXon~poxbpiTRENQErCVgsVE6iTZqqY4a8aFhrlrogYjlH2io8d8xDHxN6eAH~-Yrwb8nJ0-zTcJWe3aNPyb-EUfzfKNkbzG~pN51kty0SYTKj1HKL1FPNzIJeIgE6o1tC39vyjNfCqcw__&Key-Pair-Id=APKAJT6QIWSKVYK3V34A'
                        response = requests.get(videoLink)   
                        print("videoname", videoname)
                        with open(videoname, 'wb') as f:
                            f.write(response.content)
                        exitVal = exitVal + 1
                    if exitVal == 1:
                        print("exit================>")
                        break
                    #   filename = max([download_folder + "\\" + f for f in os.listdir(download_folder)],key=os.path.getctime)
                    #   shutil.move(filename,os.path.join(download_folder, pdfName))
                time.sleep(3)
            exitVal = 0
            print("continue================>")
            driver.switch_to.default_content()
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
