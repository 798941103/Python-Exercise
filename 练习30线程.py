import time,threading,multiprocessing

def loop():
    print('thread %s is running...' % threading.current_thread().name)      #threading.current_thread().name返回线程本身的name属性
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name,n))
        time.sleep(0.5)
    print('thread %s is ended.' % threading.current_thread().name)

t = threading.Thread(target = loop,name = 'LoopThread')         #创建一个线程LoopThread
t.start()                              #开始线程
t.join()                               #等待线程执行完毕
print('thread %s is ended.' % threading.current_thread().name)

#Lock
balance = 0
lock = threading.Lock()         #锁要放在外面，否则会生成两个内部锁，两者各自无关

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()          #获取锁
        try:
            change_it(n)        #更改
        finally:
            lock.release()      #释放锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)




'''
#死循环线程
def loop():
    x = 0
    while True:
        x = x
for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target = loop)
    t.start()
'''
'''
#多个死线程(CPU占满)
import multiprocessing
from multiprocessing import Pool,Process
import threading

def loop(i):
    x = 0
    print('Thread - ',i)
    while True:
        x = x ^ 1

def proc(i, cpu_cout):
    print('Process: ',i)
    for i in range(cpu_cout*2):
        t = threading.Thread(target=loop, args=(i,))
        t.start()

if __name__ == '__main__':
    cpu_cout = multiprocessing.cpu_count()
    p = Pool(cpu_cout)
    for i in range(cpu_cout):
        p.apply_async(proc,args=(i, cpu_cout))
    p.close()
    p.join()
'''