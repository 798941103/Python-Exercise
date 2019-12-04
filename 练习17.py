#super()
class A(object):
    def __init__(self):
        print('Enter A')
        print('Leave A')
class B(A):
    def __init__(self):
        print('Enter B')
        print('Leave B')
class C(A):
    def __init__(self):
        print('Enter C')
        print('Leave C')
class D(A):
    def __init__(self):
        print('Enter D')
        print('Leave D')
class E(B,C,D):
    def __init__(self):
        print('Enter E')
        print('Leave E')   
E()
print('\n')


class A1:
  def __init__(self):
    print("Enter A")
    print("Leave A")
class B1(A1):
  def __init__(self):
    print("Enter B")
    A1.__init__(self)
    print("Leave B")
class C1(A1):
  def __init__(self):
    print("Enter C")
    A1.__init__(self)
    print("Leave C")
class D1(A1):
  def __init__(self):
    print("Enter D")
    A1.__init__(self)
    print("Leave D")
class E1(B1, C1, D1):
  def __init__(self):
    print("Enter E")
    B1.__init__(self)
    C1.__init__(self)
    D1.__init__(self)
    print("Leave E")

E1()
print('\n')

class A2(object):
    def __init__(self):
        print('Enter A')
        print('Leave A')
class B2(A2):
    def __init__(self):
        print('Enter B')
        super().__init__()
        print('Leave B')
class C2(A2):
    def __init__(self):
        print('Enter C')
        super().__init__()
        print('Leave C')
class D2(A2):
    def __init__(self):
        print('Enter D')
        super().__init__()
        print('Leave D')
class E2(B2,C2,D2):
    def __init__(self):
        print('Enter E')
        super().__init__()
        print('Leave E')  
E2()