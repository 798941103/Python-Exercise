import subprocess

from multiprocessing import Process, Queue,Pool
import os, time, random


'''
# 子进程要执行的代码 
def run_proc(name):             #进程要执行的代码
    print('Run child process %s (%s)...' % (name, os.getpid())) 
     
if __name__=='__main__': 
    print('Parent process %s.' % os.getpid()) 
    p = Process(target=run_proc, args=('test',))    #创建一个进程，Process的第一个参数是执行函数，第二个参数是函数的参数
    print('Child process will start.') 
    p.start()                   #开始这个进程
    p.join()                    #等待进程执行完
    print('Child process end.')
    p.close()                   #关闭这个进程
'''

'''
#进程池：批量创建子进程
def long_time_task(name):       
    print('Run task %s (%s)...' % (name, os.getpid()))      #os.getpid():获得这个进程的号码
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)                                         #创建一个进程池，容量为4个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))        #创建5个进程，name为1-5,注意：方式与单个进程不同！
    print('Waiting for all subprocesses done...')
    p.close()                                           #进程池关闭，但里头的进程会继续
    p.join()                                            #等待进程池内所有进程执行完成，会先执行4个在执行1个
    print('All subprocesses done.')                     #一共有6个进程，一个主进程（开关进程池、输出最后一句），五个进程
 
'''

'''
#子进程
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])     #执行命令，返回命令的结果和执行状态，0或者非0
print('Exit code:', r)
'''

#数据传递

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)                            #输出数据
        time.sleep(random.random())             #随机推迟进程0~1秒

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)                     #接收数据
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()                                 #创建进程通信的Queue，相当于创建了一个通道
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()