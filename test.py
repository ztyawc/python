import requests
import re
def login():
    headers = {
        'Host': 'hualeshe.com',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua-platform': 'Android',
        'origin': 'https://hualeshe.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://hualeshe.com/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
    }

    data = {
        'action': 'user_login',
        'username': 'ztyawc',
        'password': 'zty123456'
    }

    response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    a = response.headers['set-cookie']
    p = re.compile(r'wordpress_logged_in.*')
    for one in p.findall(a):
        a = str(one)
    a=a.split("; ", 1)[0]
    print(a)
    return a