import turtle
bob = turtle.Turtle()

print(bob)

def koch(t, length, n):
    if n ==0 :
        return
    else:
        angle = 60
    
        koch(t, length, n-1)
        
        t.fd(length/3)
        t.lt(angle)

        koch(t, length, n-1)
        
        t.fd(length/3)
        t.rt(angle*2)

        koch(t, length, n-1)
        
        t.fd(length/3)
        t.lt(angle)

        koch(t, length, n-1)

bob.bk(600)
bob.rt(90)
bob.fd(300)
bob.lt(90)

koch(bob, 20, 5)
