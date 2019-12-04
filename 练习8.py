# -*- coding: utf-8 -*-
from functools import reduce
#1
def normalize(name):
    result = name[0].upper() + name[1:].lower()
    return result
#测试:
L1 = ["adam", "LISA", "barT"]
L2 = list(map(normalize, L1))
print(L2)

#2 
def prod(L):
    return reduce(lambda x, y : x * y, L)
#测试:
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')