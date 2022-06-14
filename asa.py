import requests
import json
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
    'cookie': 'wordpress_logged_in_420a9792b7082fc5c0fde63b2fa51820=ztyawc%7C1655349108%7C6RQazP5RMrkF5tJ7xbySv7Cw7pYEYdoul7zstjL5pvU%7Cacfa56791fca437d624c653c16c4e636e29008f8d104e938ea86bdb2fbfa43d6',
}

data = {
  'action': 'user_qiandao'
}

response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php', headers=headers, data=data)
print(response.json())

