from multiprocessing import Process, Queue,Pool
import os, time, random
def action1(a, b=20):
    for i in range(b):
        print(a, os.getpid(), ' ', i)  
        time.sleep(0.1)
def action2(a, b):
    for i in range(b):
        print(a, os.getpid(), ' ', i+1)  
        time.sleep(0.1)
def action3(a, b):
    for i in range(b):
        print(a, os.getpid(), ' ', i+2)  
        time.sleep(0.1)

if __name__ == '__main__':

    ci = Pool(3) 
    ci.apply_async(action1, args=('进程一',))  
    ci.apply_async(action2, args=('进程二', 30))
    ci.apply_async(action3, args=('进程三', 40)) 

    ci.close()  
    ci.join() 
    print('End')


def function1(n):
    _sum = 0
    for i in range((n + 2)*3):
        _sum = _sum + i*i
        print('进程 %s (%s)...' % (n, os.getpid()),_sum)
        time.sleep(0.1)

if __name__ == '__main__':
    p = Pool(4)
    for i in range(4):
        p.apply_async(function1,args = (i,))
    print('Child process will start.')
    p.close()
    p.join()
    print("End")