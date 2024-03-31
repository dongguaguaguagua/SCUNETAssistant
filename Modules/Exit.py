import sys
import time
from Modules.staticINFO import *


def app_exit(delay_time):
    print('\033[1;93m' + '[自动退出]' + '\033[0m' + '程序即将自动退出')
    time.sleep(delay_time)
    sys.exit()


def logout():
    try:
        url = main_url + "eportal/InterFace.do?method=logout"
        logout_req = requests.post(url, data='')
        if logout_req.status_code == 200:
            print('\033[1;92m' + '[成功退出登录]' + '\033[0m')
            return 0
    except requests.exceptions.ConnectionError:
        return -1
