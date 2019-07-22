def sec(z):
    prod = fir(z,z)
    print (z, prod)
    return prod

def fir(x, y):
    x = x + 1
    return x*y

def thi(a, b, c):
    total = a + b + c
    square = sec(total)**2
    return square

x = 1
y = x +1
print (thi(x, y+3,x + y))
