def fib(max): 
    n, a, b = 0, 0, 1 
    while n < max:
        print (b)
        a, b = b, a + b 
        n = n + 1
    return 'done'

def function():
    n = eval(input("Input:"))
    fib(n)
function()