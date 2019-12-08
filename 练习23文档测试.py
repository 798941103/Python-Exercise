#对函数fact(n)编写doctest并执行：
# -*- coding: utf-8 -*-

def fact(n):
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    90
    >>> fact(-1)
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':      #当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest
    import doctest
    doctest.testmod()
