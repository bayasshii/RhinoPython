def fanctorial (n):
    if n ==0:
        return 1
    else:
        a = n * fanctorial(n-1)
        return a
