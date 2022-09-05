import requests
def datong():
    headers = {
        'Host': 'www.sxydwx.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://www.sxydwx.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.25(0x18001927) NetType/WIFI Language/zh_CN',
        'Connection': 'keep-alive',
        'Referer': 'http://www.sxydwx.cn/market/marketplatfront/marketplat/sign_sx/signSX/skipView.do?appId=A12&openId=F9DC74F2D5FAD4AAC1368FC3F46751EE62D68F085F05D13F4C6201BC5EBE4729',
    }

    data = {
        'appId': 'A12',
        'openId': 'F9DC74F2D5FAD4AAC1368FC3F46751EE62D68F085F05D13F4C6201BC5EBE4729',
    }

    response = requests.post('http://www.sxydwx.cn/market/marketplatfront/marketplat/sign_sx/signSX/sign.do',
                             headers=headers, data=data)
    print(response.json()['msg'])
def shanxi():
    headers = {
        'Host': 'sx.10086.cn',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://sx.10086.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.25(0x18001927) NetType/WIFI Language/zh_CN',
        'Connection': 'keep-alive',
        'Referer': 'http://sx.10086.cn/market/marketplatfront/marketplat/sign_sx/signSX/skipView.do?appId=A100&openId=84547AFDA69C8C13FF7210B949715542EDCFF3CD5BD0C12990BA533E7F22EC64&orgId=%5Bobject+HTMLInputElement%5D',
    }

    data = {
        'appId': 'A100',
        'openId': '84547AFDA69C8C13FF7210B949715542EDCFF3CD5BD0C12990BA533E7F22EC64',
    }

    response = requests.post('http://sx.10086.cn/market/marketplatfront/marketplat/sign_sx/signSX/sign.do',
                             headers=headers, data=data)
    print(response.json()['msg'])
datong()
shanxi()