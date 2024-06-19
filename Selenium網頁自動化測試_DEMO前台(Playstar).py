from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ============================Section.1 進入遊戲大廳============================

driver = webdriver.Chrome()
driver.get("https://demo.iplaystar.net/")   # 進入 DEMO前台網頁

game_lobby = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]")))
game_lobby.click()   
print("進入DEMO前台大廳!")

# ============================Section.2 登入遊戲帳號============================

login_form = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]')))

cancel = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[6]/div[2]/input')))
cancel.click()  # 初次進入遊戲大廳會跳出登入功能選單，需先關閉方可進行後續測試。
time.sleep(2)

login_icon = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')))
login_icon.click()  # 再次點選登入功能進入選單
time.sleep(2)

check_box = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[6]')))
cancel_btn = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[6]/div[2]/input')
actions = ActionChains(driver)
actions.move_to_element(cancel_btn)    
actions.perform()
cancel_btn.click()   # 取消登入並返回遊戲大廳
time.sleep(2)

login_icon = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')))
login_icon.click()  # 再次點選登入功能進入選單
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
input_acc.send_keys("xxxxx")   # xxxxx = 個人使用者帳號
time.sleep(1)
input_acc.send_keys(Keys.TAB)   # 切換至密碼輸入欄位
input_pass.send_keys("xxxxx")  # xxxxx = 個人密碼
time.sleep(1)

rem_acc = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[4]/div/div/label')))
rem_acc.click()    # 勾選在這部電腦上記住我的帳號
time.sleep(2)

canrem_acc = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[4]/div/div/label')))
canrem_acc.click()    # 取消勾選在這部電腦上記住我的帳號
time.sleep(1)

check_box = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login-form"]/div[6]')))
confirm_btn = driver.find_element(By.XPATH, '//*[@id="login-form"]/div[6]/div[1]/input')
actions = ActionChains(driver)
actions.move_to_element(confirm_btn)    
actions.perform()
confirm_btn.click()  # 確認並登入
print("已正常登入!")
time.sleep(3)

# ============================Section.3 切換語系============================

web_lge = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]')))
actions = ActionChains(driver)
actions.move_to_element(web_lge)    
actions.perform()
# web_lge.click()

lge_en = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "en-US")))
lge_en.click()
print('網頁語系已切換為"英文"')

time.sleep(3)
web_lge = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]')))
actions = ActionChains(driver)
actions.move_to_element(web_lge)    
actions.perform()
# web_lge.click()

lge_ko = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'ko-KR')))
lge_ko.click()
print('網頁語系已切換為"韓文"')
time.sleep(3)

# ============================Section.4 修改密碼============================

setting_icon = WebDriverWait(driver, 3).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]')))
actions = ActionChains(driver)
actions.move_to_element(setting_icon)    
actions.perform()
# setting_icon.click()

pass_ch = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/a[1]')
actions = ActionChains(driver)
actions.move_to_element(pass_ch)    
actions.perform()
pass_ch.click()  # 進入修改密碼功能清單

pass_old = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="change-pwd-form"]/div[2]/input')))
pass_old.send_keys("xxxxx")   # xxxxx = 輸入舊密碼
time.sleep(1)

pass_new = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="change-pwd-form"]/div[3]/input')))
pass_new.send_keys("xxxxx")  # xxxxx = 輸入欲變更新密碼
time.sleep(1)

pass_new_1 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="change-pwd-form"]/div[4]/input')))
pass_new_1.send_keys("xxxxx")  # xxxxx = 再次輸入欲變更新密碼
time.sleep(1)

pass_chk = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="change-pwd-form"]/div[6]/div[1]/input')))
actions.move_to_element(pass_chk)    
actions.perform()
pass_chk.click()    # 新密碼變更確認
print("密碼變更成功!")

# ============================Section.5 切換遊戲選單功能============================

poker_item = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/ul/li[2]/a/span')))
actions = ActionChains(driver)
actions.move_to_element(poker_item)   # 將滑鼠游標移至"棋牌遊戲"切換選單
actions.perform()
poker_item.click()
time.sleep(2)
print("已切換至棋牌遊戲選單")

fish_item = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/ul/li[3]/a/span')))
actions = ActionChains(driver)
actions.move_to_element(fish_item)   # 將滑鼠游標移至"捕魚機"切換選單
actions.perform()
fish_item.click()
time.sleep(2)
print("已切換至捕魚機遊戲選單")

machine_item = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/ul/li[4]/a')))
actions = ActionChains(driver)
actions.move_to_element(machine_item)   # 將滑鼠游標移至"街機"切換選單
actions.perform()
machine_item.click()
time.sleep(2)
print("已切換至街機遊戲選單")

tiger_item = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/ul/li[1]/a')))
actions = ActionChains(driver)
actions.move_to_element(tiger_item)   # 將滑鼠游標移至"老虎機"切換選單
actions.perform()
tiger_item.click()
time.sleep(2)
print("已切換至老虎機遊戲選單")
time.sleep(3)

# ============================Section.6 選擇遊戲並進入主畫面============================

# -------------------------遊戲.1 財神爸爸-------------------------
god_wealth = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[6]/div')))
actions = ActionChains(driver)
actions.move_to_element(god_wealth)
actions.perform()

play_btn = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[6]/div/div/div')))
play_btn.click()
print('已點選"財神爸爸"並載入')

game_gen =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="normal"]/div')))  # 選擇一般遊戲模式
actions = ActionChains(driver)
actions.move_to_element(game_gen)
actions.perform()
game_gen.click()
print("已選取一般遊戲模式!")
print('進入"財神爸爸"主畫面')
mode_close = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'close-modal')))
actions = ActionChains(driver)
actions.move_to_element(mode_close)
actions.perform()
mode_close.click()

time.sleep(10)
driver.switch_to.window(driver.window_handles[1])  # 切換至遊戲瀏覽器分頁
driver.close()
print('已退出"財神爸爸"主畫面')
# -------------------------遊戲.2 幸運王牌-------------------------
driver.switch_to.window(driver.window_handles[0])  # 切換至原始瀏覽器分頁
# driver.get("https://demo.iplaystar.net/")

game_lobby = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]')))

lucky_ace = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[8]/div')))
actions = ActionChains(driver)
actions.move_to_element(lucky_ace)
actions.perform()

play_btn_1 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="SLOT"]/div[8]/div/div/div')))
actions = ActionChains(driver)
actions.move_to_element(play_btn_1)
actions.perform()
play_btn_1.click()
print('已點選"幸運王牌"並載入')

game_spec =  WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="feature"]/div')))  # 選擇特色遊戲模式
actions = ActionChains(driver)
actions.move_to_element(game_spec)
actions.perform()
game_spec.click()
print("已選取特色遊戲模式!")
print('進入"幸運王牌"主畫面')
mode_close_1 = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, 'close-modal')))
actions = ActionChains(driver)
actions.move_to_element(mode_close_1)
actions.perform()
mode_close_1.click()

time.sleep(10)
driver.switch_to.window(driver.window_handles[1])  # 切換至遊戲瀏覽器分頁
driver.close()
print('已退出"幸運王牌"主畫面')

# ============================Section.7 登出遊戲帳號============================

driver.switch_to.window(driver.window_handles[0])  # 切換至原始瀏覽器分頁
setting_icon = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]')))
actions.move_to_element(setting_icon)    
actions.perform()
setting_icon.click() 

logout = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/a[3]')
actions.move_to_element(logout)    
actions.perform()
logout.click() 
print("已登出!")

# ============================Section.8 再次點選登入選項確認============================

login_panel = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]')))
actions.move_to_element(login_panel)    
actions.perform()
login_panel.click()    # 再次點選登入功能鍵確認帳號已登出

# ============================Section.9 關閉瀏覽器(測試結束)============================

time.sleep(3)
driver.close()
print("瀏覽器已關閉，自動化測試結束!")