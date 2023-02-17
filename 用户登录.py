path="E:\VSCODE\CODEfield\CODE_PY\homework\\"   #此处修改成你的文件夹路径
user_path=path+"users.txt"
from copy import deepcopy
from operator import truediv
import os
from tkinter import N
def inputerror():
    print("your input is invalid, please input again")
def login(user_name, password):
    with open(user_path, 'r', encoding='utf-8') as fpr:
        for line in fpr:
            line=line.strip()
            line_list=line.split()
            if line_list[0]==user_name and line_list[1]==password:
                print("loading...")
                fpr.close()
                return True
        return False
def regist():
    while True:
        user_name=input("please input yor user name\n")
        if user_exit(user_name):
            print("the use_name already exists")
            continue
        else:
            break
    password=input("please input your password\n")
    with open(user_path, 'a', encoding='utf-8') as fpw:
        name=input("input real name\n")
        id=input("input id\n")
        score=password_score(password)      #干脆把所有信息处理为字符串
        fpw.write('\n')
        fpw.write(user_name+" "+password+" name:"+name+" id:"+id+" 密码等级:"+score)
    fpw.close()
    print("regist successfully!")
def info(user_name, password):          #注意实现修改密码功能
    with open(user_path, 'r+', encoding='utf-8') as fpr:    #对于'r+'来说，如果先读取了内容，再写入的话就变成了追加的模式，如果直接写入内容，就是覆盖了
        lines=fpr.readlines()                               #修改文件，先将所有文件读下来，后续在列表更改完读回去
        for index, line in enumerate(lines):
            kv=line.strip().split(' ')
            if kv[0]==user_name and kv[1]==password:
                print("log in successfully")
                print(kv[2], kv[3], kv[4])
                while True:                   
                    op=int(input("press 1 to change password or 2 to exit\n")) #添加功能即不小心按错    while true
                    if op!=1 and op!=2:
                        inputerror()
                        continue
                    else:
                        break
                if op==1:
                    while True:
                        new=input("new password is\n")
                        score=password_score(new)
                        print("您的密码等级为：%s, 是否需要重新修改" %score)
                        while True:                           
                            oop=input("press y or n\n")
                            if oop!='y' and oop!='n':
                                inputerror()
                                continue
                            else:
                                break
                        if oop=='y':
                            continue
                        elif oop=='n':
                            break
                    lines[index]=lines[index].replace(kv[1], new)
                    lines[index]=lines[index].replace(kv[4], score)
                    fpr.close()
                    open(user_path, 'w', encoding='utf-8').writelines(lines)
                    print("change successfully, now please log in again")
                    break
                if op==2:
                    break
def password_score(password):
    strlen=len(password)
    number=letter=mark=tag1=tag2=0
    #password=password.split()  这个地方不用split，split会将部分作为整体，直接按字符串去遍历即可
    def check(password):
        for c in password:
            if c.isnumeric():
                nonlocal number
                number+=1
            elif 'a'<=c<='z' or 'A'<=c<='Z':
                nonlocal letter, tag1, tag2
                letter+=1
                if 'a'<=c<='z':
                    tag1=1
                if 'A'<=c<='Z':
                    tag2=1
            else:
                nonlocal mark
                mark+=1
    check(password)
    def score():
        nonlocal number, letter, mark, tag1, tag2, strlen
        if strlen <=4:
            s1=5
        elif 5<=strlen<=7:
            s1=10
        else:
            s1=25
        if letter==0:
            s2=0
        elif (tag1==0 and tag2==1) or (tag1==1 and tag2==0):
            s2=10
        else:
            s2=20
        if number==0:
            s3=0
        elif number==1:
            s3=10
        else:
            s3=20
        if mark==0:
            s4=0
        elif mark==1:
            s4=10
        else:
            s4=25
        if (tag1==1 and tag2==1) and (number>0) and (mark>0):
            s5=5
        elif (tag1==1 or tag2==2) and (number>0) and (mark>0):
            s5=3
        elif (tag1==1 or tag2==2) and (number>0):
            s5=2
        else:
            s5=0
        return (s1+s2+s3+s4+s5)
    sumscore=score()
    if sumscore>=90:
        ret="非常安全"
    elif sumscore>=80:
        ret="安全"
    elif sumscore>=70:
        ret="强"
    elif sumscore>=60:
        ret="强"
    elif sumscore>=50:
        ret="一般"
    elif sumscore>=25:
        ret="弱"
    elif sumscore>=0:
        ret="非常弱"
    return ret
def user_exit(user_name):
    with open(user_path, 'r', encoding='utf-8') as fpr:
        for line in fpr:
            line=line.strip()
            line_list=line.split()
            if line_list[0]==user_name:
                return True
        return False
def main():
    print("welcome to python, please select your option")
    while True:     
        while True:
            op1=int(input("press 1 to log in, or press 2 to regist a new account\n"))
            if op1!=1 and op1!=2:
                inputerror()
                continue
            else:
                break
        if op1==1:
            user_name=input("please input yor user name\n")
            password=input("please input your password\n")
            if login(user_name, password):
                info(user_name, password)
            else:
                print("user name or password is wrong")
                op2=int(input("press 1 to return home and press 2 to exit\n"))
                if op2==1:
                    continue
                if op2==2:
                    break
        if op1==2:

            regist()
            while True:                    
                op3=int(input("press 1 to return home or 2 to exit\n"))
                if op3!=1 and op3!=2:
                    inputerror()
                    continue
                else:
                    break
            if op3==1:
                    continue
            if op3==2:
                    break
main()


