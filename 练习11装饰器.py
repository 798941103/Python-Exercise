#装饰器
# -*- coding: utf-8 -*-
import functools,time
def log(func):
    def wrapper(*args, **kw):
        #*args是非关键字参数，用于元组，**kw是关键字参数，用于字典,wrapper()函数可以接受任意参数的调用
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log                #相当于执行了now = log(now)
def now():
    print('2019-11-28')
now()


def log1(text):
    def decorator(func):
        @functools.wraps(func)          #将原始函数的属性复制到返回函数中
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log1('execute')           #相当于 now = log('execute')(now)
def now1():
    print('2019-11-28')
now1()

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        t1 = time.time()
        a = fn(*args,**kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - t1))
        return fn(*args,**kw)
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')