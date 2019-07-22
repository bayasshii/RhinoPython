import turtle
bob = turtle.Turtle()

print(bob)

def koch(t, length, n):

    if n ==0  :
        bob.fd(length)
        return
    else:
        angle = 60
    
        koch(t, length, n-1)
        
        t.fd(length)
        t.lt(angle)

        koch(t, length, n-1)
        
        t.fd(length)
        t.rt(angle*2)

        koch(t, length, n-1)
        
        t.fd(length)
        t.lt(angle)

        koch(t, length, n-1)
        
        

def snowflake(n):

    s = 120

    t = bob
    length = 30 / n**2
    
    for i in range(3):
        koch(t, length, n)
        bob.rt(s)


snowflake(0)

