def fibonacci(n):
    #base condition
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
fibonacci(6)