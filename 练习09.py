# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

def by_score(t):
    return t[1]

L1=sorted(L,key=by_name)
L2=sorted(L,key=by_score)
print(L1)
print(L2)