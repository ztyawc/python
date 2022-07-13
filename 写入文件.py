with open('data.txt','a') as f:    #设置文件对象
    str="sfsddgdfgfd";
    f.write(str+'\n')                 #将字符串写入文件中
    f.close()