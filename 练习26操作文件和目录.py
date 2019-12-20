#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import datetime
import os

pwd = os.path.abspath('.')          #查看当前目录的绝对路径
os.path.join('D:\Anaconda','Test')  #在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
os.mkdir('D:\Anaconda\Test')        #然后创建一个目录

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):           #获取该目录下的文件
    fsize = os.path.getsize(f)      #获取文件长度
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')              #获取最后的修改时间
    flag = '/' if os.path.isdir(f) else ''                                                      #获取文件名字
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))                                           #输出文件信息
os.rmdir('D:\Anaconda\Test')        #删掉一个目录


#1利用os模块编写一个能实现dir -l输出的程序。

#2编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
