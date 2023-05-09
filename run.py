import sys
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

# it's for creating pdf
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
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

driver.get('https://student.emeritus.org/courses/4208/modules')

mailPath = '//*[@id="student_email"]'
mailSubmitPath = '/html/body/main/div/div/div/form/input[2]'
passwordPath = '//*[@id="user_password"]'
passwordSubmitPath = '//*[@id="new_user"]/input[4]'

totalCoursePath = '//*[@id="context_modules"]'
titlePath = '//*[@id="context_module_item_812921"]/div/div[1]/div[1]/span/a'
module2Path = '//*[@id="context_module_content_55402"]/ul'

moduleHeaderClass = 'ig-header header'
moduleHeaderPath = './div[1]'
moduleNamePath = './span[3]/span'
# logs = driver.get_log("performance")
# print(logs)
time.sleep(1)
driver.find_element(By.XPATH, mailPath).send_keys('rajatnathan@icloud.com')
time.sleep(1)
driver.find_element(By.XPATH, mailSubmitPath).click()

time.sleep(1)
driver.find_element(By.XPATH, passwordPath).send_keys('deggu0-hiskaz-cebJed')
time.sleep(1)
driver.find_element(By.XPATH, passwordSubmitPath).click()
time.sleep(50)

totalCourse = driver.find_element(By.XPATH, totalCoursePath)
courses = totalCourse.find_elements(By.XPATH, './div')
moduleId = 0
with open('lesson.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  for c in range(0, len(courses)):
    moduleName = courses[c].find_element(By.XPATH, moduleHeaderPath).find_element(By.XPATH, moduleNamePath).get_attribute('innerHTML')
    print('module name: ', moduleName)
    # writer.writerows([str(moduleId), moduleName])
    moduleId = moduleId + 1
    modulelists = courses[c].find_element(By.XPATH, './div[2]/ul').find_elements(By.XPATH, './li')
    for l in range(0, len(modulelists)):
      if len(modulelists[l].find_elements(By.TAG_NAME, 'a')) > 0:
        lessonName = modulelists[l].find_elements(By.TAG_NAME, 'a')[0].get_attribute('title')
        lessonlink = modulelists[l].find_elements(By.TAG_NAME, 'a')[0].get_attribute('href')
        print(lessonName)
        print(lessonlink)
        writer.writerow([moduleName, lessonName, lessonlink])

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