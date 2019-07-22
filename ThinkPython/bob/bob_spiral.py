import turtle
import math as ma

bob = turtle.Turtle()

print(bob)

def archimedes_spiral(t, a):

    # t = turtle_name

    for i in range(a):
        t.fd(i/10)
        t.lt(10)
        
archimedes_spiral(bob, 300)


