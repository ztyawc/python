import pymysql

def select(sql):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='hualeshe')
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
def insert(sql):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', charset='utf8', db='hualeshe')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()