#对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
# -*- coding: utf-8 -*-

import json

import pickle

d = dict(name='Bob', age=20, score=88)
data = pickle.dumps(d)                      #pickle.dumps()方法把任意对象序列化成一个bytes
print(data)

reborn = pickle.loads(data)     #pickle.loads()方法反序列化出对象，将对象从磁盘读到内存
print(reborn)

print("\n")

#JSON
d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)                    #dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object
print('JSON Data is a str:', data)
reborn = json.loads(data)               #用loads()或者对应的load()方法反序列化
print(reborn)

class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def __str__(self):
        return 'Student object (%s, %s, %s)' % (self.name, self.age, self.score)        #转换函数，转换出一个dict

s = Student('Bob', 20, 88)
std_data = json.dumps(s, default=lambda obj: obj.__dict__)  #接收对象的dict
print('Dump Student:', std_data)
rebuild = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(rebuild)

print("\n")

#题
obj = dict(name='小明', age=20)
s1 = json.dumps(obj, ensure_ascii=True)

print(s1)

s2 = json.dumps(obj, ensure_ascii=False)        #True输出保证将所有输入的非ASCII字符转义。如果确保ensure_ascii为False，这些字符将原样输出。

print(s2)

