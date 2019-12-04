#埃拉托色尼筛选法
def _iter():#生成无限奇数序列的生成器
    n = 1
    while True:
        n = n + 2
        yield n
 
def  _filter(n):#定义筛选函数
    return lambda x:x % n > 0
 
def primes():
    yield 2          #先返回一个2
    it = _iter()     # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_filter(n), it) # 构造新序列
b = int(input('Input N:'))
for n in primes():
    if n < b:
        print(n)
    else:
        break
