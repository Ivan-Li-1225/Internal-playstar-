from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pag
from selenium.webdriver.chrome.service import Service

# ============================Section.1 進入遊戲大廳============================

driver = webdriver.Chrome()
driver.get("https://dev.iplaystar.net/")   # 進入 DEV前台網頁

lobby = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "header-box")))
lobby.click()   
print("進入DEV前台大廳!")

web_lge = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/i')))
actions = ActionChains(driver)
actions.move_to_element(web_lge)    
actions.perform()

lge_en = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'en-US')))
lge_en.click()
print("已切換英文語系!")

ps_00133 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[18]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00133)
time.sleep(2)

ps_00132 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[29]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00132)
time.sleep(2)

ps_00123 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[35]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00123)
time.sleep(2)

ps_00115 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[42]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00115)
time.sleep(2)

ps_00108 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[48]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00108)
time.sleep(2)

ps_00103 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[53]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00103)
time.sleep(2)

ps_00097 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[59]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00097)
time.sleep(2)

ps_20065 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[67]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_20065)
time.sleep(2)

ps_00087 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[79]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00087)
time.sleep(2)

ps_00072 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[93]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00072)
time.sleep(2)

ps_00057 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[108]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00057)
time.sleep(2)

ps_00048 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[117]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00048)
time.sleep(2)

ps_00038 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[127]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00038)
time.sleep(2)

ps_00025 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[140]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00025)
time.sleep(2)

ps_00017 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[148]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00017)
time.sleep(2)

ps_00006 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[159]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00006)
time.sleep(2)

go_top = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/i')))
go_top.click()
print("回到最上層!")

web_lge = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/i')))
actions = ActionChains(driver)
actions.move_to_element(web_lge)    
actions.perform()

lge_zh = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'zh-TW')))
lge_zh.click()
print("已切換繁體中文語系!")


time.sleep(2)
driver.close()
print("瀏覽器已關閉，DEV前台自動化測試結束!")