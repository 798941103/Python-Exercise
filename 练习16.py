#@preperty
'''
# -*- coding: utf-8 -*-
#定义方法，限制输入的数
class Student(object):
    def get_score(self):
         return self._score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#简化调用方法，使方法可以像属性一样被调用
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
#只读属性
class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def age(self):
        return 2015 - self._birth
'''


class Screen(object):
    @property
    def width(self):
        return _width
    @property
    def height(self):
        return _height

    @width.setter
    def width(self,value):
        if value < 0:
            raise ValueError('width must over zore')
        self._width = value
    @height.setter
    def height(self,value):
        if value < 0:
            raise ValueError('height must over zore')
        self._height = value
    
    @property
    def resolution(self):
        self._resolution = self._height * self._width
        return self._resolution

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')