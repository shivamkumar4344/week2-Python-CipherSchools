# Fibonacci series
# 0 1 1 2 3 5 8 13 21 34

def fibonacci_series(n):
    n1 = 0
    n2 = 1
    if n == 1:
        print(n1)
    elif n == 2:
        print(n1, n2)
    else:
        print(n1,n2, end =" ")
        for i in range(n-2):
            c = n1+n2
            n1=n2
            n2=c
            print(n2, end=" ")
fibonacci_series(10)
            