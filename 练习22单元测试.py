#单元测试
#对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
# -*- coding: utf-8 -*-
import unittest
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80 and self.score <= 100:
            return 'A'
        if 0 <= self.score < 60:
            return 'C'   
        raise ValueError('score must between 0~100')

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):           #只有以test_开头的方法才会在测试时执行
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':          #使代码可以被当作正常脚本运行
    unittest.main()