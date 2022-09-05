import requests
token="a478cd7133ad4744ae54af08a7f5af13"
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
if(response.json()['errorCode']=="200"):
    print("111")