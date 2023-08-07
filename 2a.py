"""Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program which accepts a
value for N (where N >0) as input and pass this value to the function. Display suitable error
message if the condition for input value is not followed."""

def fn(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn(n-1)+fn(n-2)
    
fib = int(input('Enter the position of element in the series: '))

if fib > 0:
    print('fn(',fib,')=',fn(fib),end=" ")
else:
    print('Incorrect input')