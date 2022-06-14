import requests
from zty.push import push1
from zty.test import login
headers = {
    'Host': 'hualeshe.com',
    'content-length': '19',
    'accept': '*/*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': 'Android',
    'origin': 'https://hualeshe.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://hualeshe.com/user',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': login(),
}

data = {
  'action': 'user_qiandao'
}

response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php', headers=headers, data=data)
print(response.json())
a=response.json()['msg']
a=str(a)
push1("签到",a)