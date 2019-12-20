import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()
resulit_queue = queue.Queue()
def gettask():
    return task_queue
def getresulit():
    return resulit_queue

BaseManager.register('get_task_queue',callable=gettask)
BaseManager.register('get_resulit_queue',callable=getresulit)