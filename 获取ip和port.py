import re
f = open("D:\\1.txt",encoding='utf-8')
a=f.read()
f.close()
ips=(re.findall(r'IP:\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3}--',a))
print("ip:")
for ip in ips:
    with open('D:\\ip.txt', 'a') as f:  # 设置文件对象
        ip1 = str(ip)
        ip1 = ip1.replace("IP:", "DOMAIN,")
        ip1 = ip1.replace("--", ",PROXY")
        f.write(ip1 + '\n')  # 将字符串写入文件中
        f.close()
ports=(re.findall(r'端口:.*.*--',a))
for port in ports:
    port1=str(port)
    port1=port1.replace("端口:","PORT,")
    port1=port1.replace("--",",PROXY")
    with open('D:\\port.txt', 'a') as f:  # 设置文件对象
        f.write(port1 + '\n')  # 将字符串写入文件中
        f.close()