import subprocess
import getpass
import art

if __name__ == '__main__':


    #WORKER = "worker.py"
    #WORKER = "worker"
    

    while True:
        art.art_ascii()
        
        print('==========================================================')
        print('⬇️  アカウント情報を入力  ⬇️   "r" ⇨ 情報を入力し直せます')
        print('==========================================================')
        print('ID')
        ID = input('>>> ')
        if ID == 'r':
            continue
            
        print('PASS')
        PASS = getpass.getpass('>>> ')
        if PASS == 'r':
            continue

        print('テキストパス(例:/Users~.txt)')
        TEXT_PASS_BE = input('>>> ')
        if TEXT_PASS_BE == 'r':
            continue
        TEXT_PASS_AF = 'r' + TEXT_PASS_BE

        print('ペースト ⇨ 送信までの時間間隔指定')
        print('引数指定(第一, 第二) 例:(0,3)')
        RNDM_TIME = input('>>> ')
        if RNDM_TIME == 'r':
            continue
        #パスを通した状態で"worker"を指定して直接実行する'''
        subprocess.run(["worker",  ID, PASS, TEXT_PASS_BE, RNDM_TIME])
    
