# -*- coding: utf-8 -*-

fpath1 = r'F:\text.txt'

with open(fpath1, 'w') as f:
    f.write('Hello, world!\n')

with open(fpath1, 'r') as f:
    s = f.read()
    print(s)

fpath2 = r'F:\编程学习\笔记\python笔记.txt'
with open(fpath2, 'r') as f:
    s = f.read()
    print(s)
# 运行代码观察结果
