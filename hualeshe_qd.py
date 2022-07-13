import requests
import re
import pymysql
import os
from zty.tui import push1
from lxml import etree
#获取cookie
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
#签到
def qd(cookie):
    headers = {
        'authority': 'hualeshe.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://hualeshe.com',
        'referer': 'https://hualeshe.com/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': cookie,
    }

    data = {
        'action': 'user_qiandao'
    }
    response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php', headers=headers, data=data)
    return response.json()['msg']
#查询积分
def jf(cookie):
    headers = {
        'authority': 'hualeshe.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': cookie,
        'referer': 'https://hualeshe.com/',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    response = requests.get('https://hualeshe.com/user', headers=headers)
    res = etree.HTML(response.text)
    jf = res.xpath('//*[@id="user-profile"]/div/div[2]/form/div[1]/div/div[1]/div/h3/text()')[0]
    jf = str(jf)
    print(jf)
    return jf
def select():
    conn = pymysql.connect(host='43.154.35.115', port=3310, user='root', passwd='123456', charset='utf8', db='hualeshe')
    cursor = conn.cursor()
    sql = "SELECT users.username FROM users"
    cursor.execute(sql)
    while True:
        row = cursor.fetchone()
        if not row:
            #读取文件并推送
            f = open("data.txt", encoding='utf-8')
            a = f.read()
            push1("签到", a)
            f.close()
            #删除文件
            os.remove('data.txt')
            break
        username=row[0]
        a=login(username)
        msg=qd(a)
        num=jf(a)
        str=username+msg+num
        with open('data.txt', 'a',encoding='utf-8') as f:  # 设置文件对象
            f.write(str + '\n')  # 将字符串写入文件中
            f.close()
select()
