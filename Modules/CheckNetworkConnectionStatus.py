from Modules.staticINFO import *


def check_network_connection_status():
    url = "http://detectportal.firefox.com/success.txt"
    try:
        if requests.get(url=url, headers=http_header,
                        proxies=proxies, timeout=5).text.strip() == 'success':
            return 0
    except requests.exceptions.ReadTimeout:
        print('\033[1;91m' + '[请求超时]' + '\033[0m' + ', 即将重试')
        return -1
    return -1
