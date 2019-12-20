# task_master.py
#主进程
import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

#由于Windows下绑定接口不能使用lambda，所以要先定义函数
def gettask():
    return task_queue
def getresult():
    return result_queue

#Windows要加freeze_support()方法，所以改成方法调用
def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable = gettask)
    QueueManager.register('get_result_queue', callable = getresult)

    # 绑定端口5000, 设置验证码'abc'(Windows下需要填写IP地址):
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动Queue:
    manager.start()

    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 执行的任务:
    for i in range(10):
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n)

    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭,否则会报错:
    manager.shutdown()
    print('master exit.')

#Windows下多进程可能会炸，所以需要加这行，也必须加这行才能运行
if  __name__ == '__main__':
    freeze_support()
    test()