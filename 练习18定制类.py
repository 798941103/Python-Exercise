#定制类
'''
#__str__()
class StrClass(object):
    def __init__(self,name):
        self.name = name
    def __str(self):
        return 'Student object (name:%s)' %self.nam
print(StrClass('Michael'))
'''

'''
#__iter__()
class FibClass(object):
    def __init__(self):
        self.a,self.b = 0 , 1
        self.x = int(input('Input Date:'))
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > self.x:
            raise StopIteration()
        return self.a
for n in FibClass():
    print(n)
'''

'''
#__getitem__
class Fibclass(object):
    def __getitem__(self,n):
        if isinstance(n,int):       #如果传入的是实数，就返回对应的值
            a,b = 1,1
            for x in range(n):
                a,b = b,a +b
            return a
        if isinstance(n,slice):     #如果传入的是切片，就返回指定的序列
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

F = Fibclass()
print(F[int(input('Input Date:'))])
'''

'''
#__getattr__
class StudentClass(object):
    def __init__(self):
        self.name = 'Michael'
    def __getatter__(self,attr):
        if arrt=='score':
            return 90
        if arrt=='age':
            return lambda :18
'''
'''
#__call__()
class Student(object):
    def __init__(self,name):
        self.name = str(input('Name: '))

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
s()
'''


#链式调用
class Chain(object):
    def __init__(self, path=''):        #赋给参数初始值
        self._path = path               #前者是已经赋值的_path属性，后者是用__getattr__获得的属性
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))          #返回类，创建一个新的对象（递归？）
    def __str__(self):
        return self._path
    __repr__ = __str__

print(Chain().status.user.timeline.list)       
#Chain().status.user.timeline.list这个式子，代表的就是chain()的status属性的user属性的timelin属性的list属性
#/status/user/timeline/list


#     example = Chain()    初始化一个实例
#     example1 = example1.status    
#查找实例c1的一个属性，因为没有这个属性，所以通过__getattr__来尝试获取status属性，接着通过__getattr__()方法返回，Chain(/status),
#此时为实例对象c2(path = '/status')
#     example2 = example2.user    
#查找实例c2的一个属性，因为没有这个属性，所以通过__getattr__来尝试获取user属性，接着通过__getattr__()方法返回，Chain(/status/user),
#此时为实例对象c3(path = '/status/user')
#    .....
#最后通过__str__()的方法打印出最后一个对象（即实例对象5）
