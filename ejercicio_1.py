def fibo_r(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo_r(n-1) + fibo_r(n-2)
    
