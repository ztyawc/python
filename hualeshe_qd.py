import requests
import re
import pymysql
import time
def login(username):
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
        'username': username,
        'password': 'zty123456'
    }

    response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    a = response.headers['set-cookie']
    p = re.compile(r'wordpress_logged_in.*')
    for one in p.findall(a):
        a = str(one)
    a=a.split("; ", 1)[0]
    return a
def qd(cookie):
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
        'cookie': cookie,
    }

    data = {
        'action': 'user_qiandao'
    }
    response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    return response.json()['msg']
def select():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='hualeshe')
    cursor = conn.cursor()
    sql = "SELECT users.username FROM users"
    cursor.execute(sql)
    while True:
        row = cursor.fetchone()
        if not row:
            break
        username=row[0]
        a=login(username)
        msg=qd(a)
        print(username+msg)
select()
