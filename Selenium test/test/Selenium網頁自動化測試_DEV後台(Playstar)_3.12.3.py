from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ============================Section.1 進入後台首頁============================

driver = webdriver.Chrome()
driver.get("https://dev-admin.iplaystar.net/")   # 進入 DEMO前台網頁

back_platform = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/form/div/div[1]")))
back_platform.click()
time.sleep(3)
print("進入DEV後台首頁!")

##  -----------切換網頁顯示語系-----------
language_bar = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/form/label')))
language_bar.click()

language_ch_zh = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="lang"]/option[2]')))
language_ch_zh.click()
print("語系已切換'繁體中文'!")

# ============================Section.2 登入使用者名稱及密碼============================

login_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'content-group')))
login_icon.click()  # 尋找登入介面元素位址
time.sleep(2)

login_acc = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="user_id"]')))
login_acc.clear()    # 預設此欄位為null, 但仍先清除帳號欄位資訊
login_pass = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))   
login_pass.clear()   # 預設此欄位為null, 但仍先清除密碼欄位資訊

actions = ActionChains(driver)
actions.move_to_element(login_acc)    
actions.perform()
login_acc.send_keys("ivan_li")   # 個人使用者帳號
time.sleep(1)
login_acc.send_keys(Keys.TAB)   # 切換至密碼輸入欄位
login_pass.send_keys("iPlaystar296")  # 個人密碼
time.sleep(1)

login_botton = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/form/div/div[6]/button')))
login_botton.click()
print("登入成功!")
time.sleep(2)

# ============================Section.3 切換後台功能頁籤============================

account = driver.find_element(By.ID, 'Accounting')
account.click()
print("進入帳務功能選單!")
time.sleep(1)

game_performance = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div/ul/li[2]/ul/li[1]/a')))
actions.move_to_element(game_performance)    
actions.perform()
game_performance.click()
print("切換遊戲績效功能!")
time.sleep(2)

account = driver.find_element(By.ID, 'Accounting')
actions.move_to_element(account)    
actions.perform()
player_performance = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div/div/ul/li[2]/ul/li[6]/a')))
actions.move_to_element(player_performance)    
actions.perform()
player_performance.click()
print("切換玩家績效功能!")
time.sleep(2)

player = driver.find_element(By.ID, 'Player')
player.click()
print("進入玩家功能選單!")
time.sleep(1)

player_info = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[2]/div[1]/div/div/ul/li[3]/ul/li[1]/a')))
actions.move_to_element(player_info)    
actions.perform()
player_info.click()
print("切換玩家資訊功能!")
time.sleep(2)

player = driver.find_element(By.ID, 'Player')
actions.move_to_element(player)    
actions.perform()
player_savefile = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div[2]/div[1]/div/div/ul/li[3]/ul/li[10]/a')))
actions.move_to_element(player_savefile)    
actions.perform()
player_savefile.click()
print("切換玩家遊戲存檔功能!")
time.sleep(2)

# ============================Section.4 返回主頁並登出============================

mainpage = driver.find_element(By.ID, 'Home')
actions.move_to_element(mainpage)    
actions.perform()
mainpage.click()
print("返回主頁!")
time.sleep(3)

logouticon = driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
actions.move_to_element(logouticon)    
actions.perform()
logouticon.click()
logout_botton = driver.find_element(By.ID, 'logout')
logout_botton.click()
print("已登出")
time.sleep(2)

exit = input("please input 'Q' to exit!")
if exit == "Q":
    driver.quit()
    print("瀏覽器已關閉，自動化測試結束!")
else:
    exit = input("please input 'Q' to exit!")
