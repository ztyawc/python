import requests
import random
import pymysql
def insert(sql):
    conn = pymysql.connect(host='43.154.35.115', port=3310, user='root', passwd='123456', charset='utf8', db='hualeshe')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
user_name="z"+str(random.randint(10,900))+"sd"+str(random.randint(30,90))
user_email=str(random.randint(100000000,900000000))+"@qq.com"
user_pass="zty123456"
headers = {
    'authority': 'hualeshe.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'PHPSESSID=n7hppq3qaptk85ophpb5vilmdm',
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
}

data = {
    'action': 'user_register',
    'user_name': user_name,
    'user_email': user_email,
    'user_pass': user_pass,
    'user_pass2': user_pass,
}

response = requests.post('https://hualeshe.com/wp-admin/admin-ajax.php',headers=headers, data=data)
print(response.json())
sql='INSERT INTO users(username,password) VALUES("{}","{}")'.format(user_name,user_pass)
insert(sql)