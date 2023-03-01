# PASAPORT-RANDEVU-NOTIFICATOR v1.0
# Author: Huseyin YILDIZ
# github: github.com/huseyin-yildiz

# ! Selenium ve playsound kutuphanlerini yuklemeyi unutmayiniz.
# ! Kötü amaçlı kullanılmamasi icin guvenlik kodu kısmını kendiniz girmeniz gerekiyor. 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from datetime import datetime
import os
from playsound import playsound


import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Webdriver başka tarayıcı ile degistirilebilir 
driver = webdriver.Firefox()
alarm_path = "./alarm.mp3"

SORGULAMA_PERIYODU = 25 #sn

############## BİLGİLER ###############
######## BU ALANI DÜZENLEYİNİZ ########

ISIM = "ISIM"
SOYISIM = "SOYISIM"
DOGUM_AY = 1
DOGUM_YIL = 2022
DOGUM_GUN = 1
TELEFON = "5555555555"
ARANAN_SEHIR = "İstanbul"

########################################




def sorgula(sehir):
    driver.find_element(By.LINK_TEXT, sehir).click()
    element = driver.find_element(By.PARTIAL_LINK_TEXT, "Doluluk Oranı")
    doluluk_percentage = int (element.text.split("%")[1].split("\n")[0])
    if(doluluk_percentage != 100):
        print(datetime.now(),": ",element.text )
        playsound(alarm_path)        


driver.get("https://randevu.nvi.gov.tr/default/step2")
driver.get("https://randevu.nvi.gov.tr/")
driver.set_window_size(1854, 1053)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "a:nth-child(3) .fs10").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".btn-default").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(3) .btn").click()
driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(1) .form-control").click()
driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(1) .form-control").send_keys(ISIM)
driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(2) .form-control").send_keys(SOYISIM)
driver.find_element(By.ID, "IdentityNo").send_keys("27217574162")
driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(1) > .nvi-number-format").send_keys(DOGUM_GUN)
driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(2) > .nvi-number-format").send_keys(DOGUM_AY)
driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(3) > .nvi-number-format").send_keys(DOGUM_YIL)
driver.find_element(By.CSS_SELECTOR, ".col-xs-12:nth-child(5) .nvi-number-format").send_keys(TELEFON)
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()
element = driver.find_element(By.CSS_SELECTOR, ".btn-lg")

time.sleep(10)

while(True):
    sorgula(ARANAN_SEHIR)
    time.sleep(SORGULAMA_PERIYODU)

