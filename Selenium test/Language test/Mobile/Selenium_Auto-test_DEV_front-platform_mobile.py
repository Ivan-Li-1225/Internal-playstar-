from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

mobile_emulation = {"deviceName": "iPhone 12 Pro"}
options = Options()
options = webdriver.ChromeOptions()
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options=options)
driver.get("https://dev.iplaystar.net/")
time.sleep(3)
print("進入DEV前台大廳!")

# ============================Section.2 登入遊戲帳號============================

login_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[1]/a')))
login_icon.click()  # 點選登入功能進入選單
time.sleep(2)
input_acc = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[2]/input')))
input_acc.clear()    # 清除帳號欄位資訊
input_pass = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[3]/input')))   
input_pass.clear()   # 清除密碼欄位資訊

actions = ActionChains(driver)
actions.move_to_element(input_acc)    
actions.perform()
input_acc.send_keys("ivan_li")   # 使用者帳號
time.sleep(1)
actions.send_keys(Keys.TAB)   # 切換至密碼輸入欄位
input_pass.send_keys("Koe1050259@")  # 密碼
time.sleep(1)

rem_acc = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[4]/div/div/label')))
rem_acc.click()    # 勾選在這部電腦上記住我的帳號
time.sleep(2)

nonrem_acc = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[4]/div/div/label')))
nonrem_acc.click()    # 取消勾選在這部電腦上記住我的帳號
time.sleep(1)
confirm_btn = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[6]/div[1]/input')
actions = ActionChains(driver)
actions.move_to_element(confirm_btn)    
actions.perform()
confirm_btn.click()  # 確認並登入

if input_acc == True and input_pass == True:
        print("登入成功!")
else:
    print("登入失敗 : 帳號或密碼錯誤!")
    time.sleep(3)

input_acc_again = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[2]/input')))
input_acc_again.clear()    # 清除帳號欄位資訊
input_pass_again = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[3]/input')))   
input_pass_again.clear()   # 清除密碼欄位資訊

actions = ActionChains(driver)
actions.move_to_element(input_acc_again)    
actions.perform()
input_acc_again.send_keys("ivan_li")   # 使用者帳號
time.sleep(1)
input_acc_again.send_keys(Keys.TAB)   # 切換至密碼輸入欄位
input_pass_again.send_keys("@Koe1050259@")  # 密碼
time.sleep(1)

confirm_btn_1 = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[6]/div[1]/input')
actions = ActionChains(driver)
actions.move_to_element(confirm_btn_1)    
actions.perform()
confirm_btn_1.click()  # 確認並登入
print("登入成功!")
time.sleep(3)

# ============================Section.3 切換語系============================

web_lge = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/i')))
actions = ActionChains(driver)
actions.move_to_element(web_lge)    
actions.perform()
web_lge.click()

lge_en = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'en-US')))
lge_en.click()
print("已切換英文語系!")

ps_00157 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[3]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00157)
time.sleep(2)

ps_00154 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[7]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00154)
time.sleep(2)

ps_00147 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[13]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00147)
time.sleep(2)

ps_00140 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[16]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00140)
time.sleep(2)

ps_00134 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[24]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00134)
time.sleep(2)

ps_00132 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[29]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00132)
time.sleep(2)

ps_00123 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[35]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00123)
time.sleep(2)

ps_00116 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[41]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00116)
time.sleep(2)

ps_00110 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[47]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00110)
time.sleep(2)

ps_00103 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[53]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00103)
time.sleep(2)

ps_00099 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[57]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00099)
time.sleep(2)

ps_00091 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[63]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00091)
time.sleep(2)

ps_20065 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[67]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_20065)
time.sleep(2)

ps_10035 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[71]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_10035)
time.sleep(2)

ps_00087 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[79]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00087)
time.sleep(2)

ps_00080 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[85]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00080)
time.sleep(2)

ps_00074 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[91]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00074)
time.sleep(2)

ps_00068 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[97]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00068)
time.sleep(2)

ps_00064 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[101]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00064)
time.sleep(2)

ps_00056 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[109]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00056)
time.sleep(2)

ps_00052 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[113]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00052)
time.sleep(2)

ps_00045 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[120]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00045)
time.sleep(2)

ps_00038 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[127]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00038)
time.sleep(2)

ps_00032 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[133]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00032)
time.sleep(2)

ps_00021 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[144]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00021)
time.sleep(2)

ps_00014 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[151]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00014)
time.sleep(2)

ps_00007 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[158]')))
driver.execute_script("arguments[0].scrollIntoView()", ps_00007)
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
web_lge.click()

lge_zh = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'zh-TW')))
lge_zh.click()
print("已切換繁體中文語系!")
time.sleep(2)

test_continue = input("請確認是否繼續測試(Y/N): ")
print(test_continue)
if test_continue == "N":
      driver.close()
      print("瀏覽器已關閉，DEV前台自動化測試結束!")

else:
      print("Continue...")