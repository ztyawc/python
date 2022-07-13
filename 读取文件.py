from zty.tui import push1
f = open("data.txt",encoding='utf-8')
a=f.read()
push1("签到",a)
f.close()