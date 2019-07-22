import turtle
import math as ma
import string as st

def draw_delta(t, l, a):

    # t = turtle_name
    # l = tyouhen
    # a = angle

    #draw_inside
    t.fd(l)
    t.lt(a+90)

    #draw_outside
    s = ma.sin(2*ma.pi*(a/360)) * l * 2 
    t.fd(s)

    
def draw_deltas(k):
    
    l = 100
    a = (180 / k)
    
    bobs = []
    for i in range(k):
        name = k
        bobs.append(name)        
        bobs[i] = turtle.Turtle()
        bobs[i].lt(i*(360/k))
         
    for i in range(k):
         draw_delta(bobs[i], l, a)

draw_deltas(100)
