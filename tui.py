import requests
def push1(title,content):
    url = "http://www.pushplus.plus/send?token=2b3181c23f5446a79ec93143310239ad&title=" + title + "&content=" + content + "&template=html"
    requests.get(url)