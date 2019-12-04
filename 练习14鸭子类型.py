#鸭子类型
class Animal(object):
    def run(self):
        print('Animal is running')
class Dog(Animal):
    def run(self):
        print('Dog is running')
class Cat(Animal):
    def run(self):
        print('Cat is running')
class People(object):
    def run(self):
        print('Poeple is running')
def _run(x):
    x.run()
_run(Animal())
_run(Cat())
_run(Dog())
_run(People())