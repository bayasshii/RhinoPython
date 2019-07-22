import turtle
import math as ma

bob = turtle.Turtle()
sapp = turtle.Turtle()

print(bob)
print(sapp)


def fermat_spiral(t1, t2, n):

    # t1 = turtle_name
    # t2 = the_other_turtle_name

    t2.lt(180)
    
    for theta in range(n):
        
        r = theta**(1.5) / 10 
        
        t1.fd(r)
        t1.lt(10)

        t2.fd(r)
        t2.lt(10)


fermat_spiral(bob, sapp, 100)
