import requests
#账号
username="sxjm2005150239"
#密码
password="zhzj@123ABC"

def login(username,password):
    headers = {
        'Host': 'user.icve.com.cn',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 whatyApp whatyApiApp',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://user.icve.com.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://user.icve.com.cn/sites/zhzj/mobile/teacherMobile/login.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'mobile': username,
        'passwd': password,
    }

    response = requests.post('https://user.icve.com.cn/m/peMobileLogin_accountLogin.action', headers=headers, data=data)
    token=response.json()['token']
    return token
def writToken():
    str = login(username, password)
    with open('token.txt', 'w') as f:  # 设置文件对象
        f.write(str)  # 将字符串写入文件中
        f.close()
        r = open("token.txt", encoding='utf-8')
        a = r.read()
        r.close()
        print("已写入新token")
        return a
def getToken():
    try:
        f = open("token.txt", encoding='utf-8')
        a = f.read()
        f.close()
        return a
    except FileNotFoundError:
        print("文件不存在")
        str = login(username, password)
        with open('token.txt', 'w') as f:  # 设置文件对象
            a=writToken()
            return a
token=getToken()
def checkToken():
    headers = {
        'Host': 'user.icve.com.cn',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 whatyApp whatyApiApp',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://user.icve.com.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    params = {
        'token': token,
    }

    response = requests.post('https://user.icve.com.cn/m/zhzjMobile_getRestSsoToken.action', params=params,
                             headers=headers)
    print(response.json())
    if (response.json()['errorCode'] == "200"):
        print("token正常,继续执行")
        return True
    else:
        print("token失效")
        writToken()
        print("请重新执行")
if __name__ == '__main__':
    if(checkToken()==True):
        print("1111")