import requests
import time
import random
nowTime=time.time()*1000
ClassIdList = {}
classroomids={}
signs={}
#账号
username="sxjm2005150239"
#密码
password="zhzj@123ABC"
#登录获取token
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
#不存在就写入token
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
#文件读取获取token
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
#检查token
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
def get_Authorization():
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
    userAccessToken = response.json()['data']['userAccessToken']
    return userAccessToken
def courseId():
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
        'Referer': 'https://user.icve.com.cn/sites/zhzj/mobile/studentMobile/index.html',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    data = {
        'pageSize': '4',
        'curPage': '1',
        'token': token,
        'type': '1',
    }

    response = requests.post('https://user.icve.com.cn/m/zhzjMobile_getMyClassList.action', headers=headers, data=data)
    ClassIds = response.json()['data']
    for ClassId in ClassIds:
        ClassIdList.update({ClassId['courseName']: ClassId['courseId']})
Authorization='Bearer '+get_Authorization()
#排除未到时间的课程
def checkTime():
    for i in ClassIdList:
        idd=ClassIdList[i]
        courseId = idd
        headers = {
            'Host': 'spoc-classroom.icve.com.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '58',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'authorization': Authorization,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 whatyApp whatyApiApp',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://user.icve.com.cn',
            'X-Requested-With': 'com.whaty.qyZHZJ',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://user.icve.com.cn/',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"params":{"courseId":' + "\"" + courseId + "\"" + '}}'

        response = requests.post(
            'https://spoc-classroom.icve.com.cn/classroom-teaching-api/classroom/getClassroomByStudent',
            headers=headers,
            data=data)
        try:
            courseName=(response.json()['data']['data']['records'][0]['courseName'])
            startDate=(response.json()['data']['data']['records'][0]['startDate'])
            id=(response.json()['data']['data']['records'][0]['id'])
        except:
            pass
        if(nowTime>=startDate):
            classroomids.update({courseName:id})
#获取签到数据
def Obtain():
    for classroomid in classroomids:
        print(classroomid)
        a=(classroomids[classroomid])
        classroomId = a
        headers = {
            'Host': 'spoc-classroom.icve.com.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '147',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': Authorization,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 whatyApp whatyApiApp',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://spoc-classroom.icve.com.cn',
            'X-Requested-With': 'com.whaty.qyZHZJ',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://spoc-classroom.icve.com.cn/classroom/mobile.html',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = '{"params":{"classroomId":' + "\"" + classroomId + "\"" + ',"classroomTypeCode":1},"page":{"curPage":1,"pageSize":10,"totalCount":0,"totalPage":0}}'

        response = requests.post(
            'https://spoc-classroom.icve.com.cn/classroom-teaching-api/peClassroomActivity/student/classroomActivityList',
            headers=headers, data=data)
        items = response.json()['data']['items']
        for item in items:
            if (item['typeName'] == "签到"):
                itemt = item
                if (itemt["status"] == "1"):
                    recordId=(itemt['recordId'])
                    id=(itemt['id'])
                    for i in classroomids:
                        signs.update({recordId:id})
#签到
def Inquire():
    for i in signs:
        headers = {
            'Host': 'spoc-classroom.icve.com.cn',
            'Connection': 'keep-alive',
            # 'Content-Length': '100',
            'Accept': 'application/json, text/plain, */*',
            'Authorization': Authorization,
            'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2012K11C Build/SQ3A.220705.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 whatyApp whatyApiApp',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://spoc-classroom.icve.com.cn',
            'X-Requested-With': 'com.whaty.qyZHZJ',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://spoc-classroom.icve.com.cn/classroom/mobile.html',
            # 'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        id = i
        activityId = signs[i]
        data = '{"params":{"id":' + "\"" + id + "\"" + ',"activityId":' + "\"" + activityId + "\"" + '}}'

        response = requests.post(
            'https://spoc-classroom.icve.com.cn/classroom-teaching-api/sign/student/updateSignStatus', headers=headers,
            data=data)
        print(response.json())
if __name__ == '__main__':
    if(checkToken()==True):
        courseId()
        checkTime()
        Obtain()
        Inquire()