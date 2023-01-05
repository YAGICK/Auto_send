#coding:utf-8
import time
import random
import sys
import os
import random

from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

option = Options()
option.add_argument('--incognito')
option.add_argument('enable-crash-reporter')
#プロファイル指定
PROFILE_PATH = r'xxxxxxxxxxxxxxxxxxxxxx'
option.add_argument('--user-data-dir=' + PROFILE_PATH)
driver = selenium.webdriver.Chrome(ChromeDriverManager().install(),options=option)
driver.set_window_size('1200', '1000')
#要素が見つかるまで、最大10秒間待機する
driver.implicitly_wait(10)
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "image/screen.png")

#**************************************************
ID = sys.argv[1]
PASS = sys.argv[2]
TEXT_PASS_BE = sys.argv[3]
RNDM_TIME = sys.argv[4]

def login_etc(your_id, your_pass):
    try:
        print("20秒以内にプロキシを設定してください")
        time.sleep(20)
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        print("-----------------------------------------------")
        print("Succcess: <URLにアクセス完了>")
        print("-----------------------------------------------")
    except:
        print("Error: <URLが見つかりませんでした>")
        driver.quit()
    try:
        # ログインIDを入力
        login_id = driver.find_element_by_name("username")
        login_id.send_keys(your_id)
        print("Succcess: <ユーザーネーム入力完了>")
        print("-----------------------------------------------")
    except:
        print("Error: <ユーザーネーム or 要素が見つかりませんでした>")
        #driver.save_screenshot(FILENAME)
        print()
    try:
        # パスワードを入力
        password = driver.find_element_by_name("password")
        password.send_keys(your_pass)
        print("Succcess: <パスワード入力完了>")
        print("-----------------------------------------------")
    except:
        print("Error: <パスワード or 要素が見つかりませんでした>")
    try:
        #ログインボタンをクリック
        driver.find_element_by_class_name('L3NKy       ').click()
        time.sleep(3)
        print("Succcess: <ログイン試行中...>")
        print("-----------------------------------------------")
    except:
        print("Error: <IDまたはPASSを確認してください>")
        print("終了:q")
        cmd = input(">>> ")
        if cmd == "q":
            driver.quit()
        
        #"後で"移動
    try:
        driver.find_element_by_css_selector('.HoLwm').click()
    except:
        #メッセージ移動
        driver.find_element_by_class_name('xWeGp').click()
        time.sleep(2)
        #"後で"移動
        driver.find_element_by_css_selector('.HoLwm').click()
        
    
    try:
        #メッセージに移動
        print("Succcess: <ログイン完了・メッセージに移動します>")
        driver.find_element_by_class_name('xWeGp').click()
        print("-----------------------------------------------")
    except:
        print("ログインできませんでした")
        print("ログイン情報を確認し再度試行してください")
        
#elementは要素を返す
#elementsは要素の配列を返す
        
def send_message_loop(chara_txt_pass, rndm_time):
    cnt = 0
    snd_cnt = 0
    num = 18
    while cnt < num:
        try:
            #リクエストを開く
            req_go = driver.find_element_by_css_selector('.gtFbE')
            req_go.click()
        except:
            print("<処理完了・リクエスト0件...>")
            driver.quit()
        try:
            #先頭に表示されるリクエストを開く
            element_top_request_path = '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[3]/div/div/div[1]/a'
            element_top_request = driver.find_element_by_xpath(element_top_request_path)
            element_top_request.click()
            #ここでsleepしないと早すぎて後が読み込めなくなる
            time.sleep(1)
        except:
            print("Error: <最上部のリクエストに移動できませんでした>")
            driver.quit()
        try:
            #リクエストを承認
            element_accept_path = '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/button/div/div'
            element_accept = driver.find_element_by_xpath(element_accept_path)
            element_accept.click()
            time.sleep(1)
        except:
            print("Error: <リクエストを承認できませんでした>")
            
        try:
            #textarea取得
            element_txtarea = driver.find_element_by_css_selector('.X3a-9 textarea')
            with open(chara_txt_pass, encoding='UTF-8') as t:
                update_txt = t.read().strip()
            #javascriptを直接実行-テキストペースト
            driver.execute_script('document.querySelector("div.X3a-9 textarea").value="%s";' % update_txt.replace('\n','\\n'))
            #スペースキー押下後送信キーが押せるようになるから
        except:
            print("Error: <テキストエリア取得 & ペーストを完了できませんでした>")
            driver.quit()
        try:
            element_txtarea.send_keys(Keys.SPACE)
        except:
            print("Error: <スペースを押せませんでした>")
            print("もう一度押します")
            time.sleep(2)
            element_txtarea.send_keys(Keys.SPACE)
        try:
            #エンター送信
            #通常時間指定
            move1 = rndm_time[0]
            move2 = rndm_time[2]
            rndm = random.randint(int(move1), int(move2))
            time.sleep(rndm)
            element_txtarea.send_keys(Keys.ENTER)
            time.sleep(1)
            cnt+=1
            snd_cnt+=1
            print('==========================================================')
            print(f'Succcess:<*******{cnt}回目送信完了******合計{snd_cnt}件>')
            print('----------------------------------------------------------')
        except:
            print("Error: <送信できませんでした>")
            driver.quit()
        try:
            if cnt == num-1:
                print('==========================================================')
                print(f'<********{(num-1)}回目なのでページを更新します********>')
                print('==========================================================')
                cnt = 0
                driver.refresh()
                #time.sleep(1)
                continue
        except:
            print("Error: <更新できませんでした>")
            driver.quit()
login_etc(ID, PASS)
send_message_loop(TEXT_PASS_BE, RNDM_TIME)
    

