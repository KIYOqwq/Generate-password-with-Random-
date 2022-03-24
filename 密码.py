import random

random.seed(0x1010) #设置随机种子
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
ls = []#存密码的列表
Firstzifu = ""#存第一个字符
while len(ls)<20:
    pwd = ""
    for i in range(10):
        pwd += s[random.randint(0,len(s)-1)]
    if pwd[0] in Firstzifu:
        continue
    else:
        ls.append(pwd)
        Firstzifu +=pwd[0]
fo = open("随机密码.txt","w",encoding ="utf-8")

fo.write("\n".join(ls))
