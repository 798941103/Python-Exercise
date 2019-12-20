import threading

_local = threading.local()      #创建一个全局ThreadLocal对象

def _Student():
    std = _local.student        #获取当前线程关联的student
    print('Hello %s (in %s)' % (std,threading.current_thread().name))

def thread(name):               #绑定ThreadLocal的student
    _local.student = name
    _Student()

t1 = threading.Thread(target = thread,args = (str(input('Input name:')),),name = 'Thread-1')
t2 = threading.Thread(target = thread,args = (str(input('Input name:')),),name = 'Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()