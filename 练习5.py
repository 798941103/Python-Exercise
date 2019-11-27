def _odd_iter():                    #生成所有整数的生成器
    n=1
    while True:
        n = n + 1
        yield n

def _not_divisible(n):                  #用于筛选的函数
    return lambda x: x % n > 0

def primes():                               #生成素数的生成器
    a = _odd_iter()
    while True:
        n = next(a)
        yield n
        a = filter(_not_divisible(n),a)

b = int(input("Input:"))
for n in primes():                          #调用函数同时设置退出条件
    if n < b:
        print(n)
    else:
        break