import turtle
bob = turtle.Turtle()

print(bob)

def draw_leaf(t, n, l, a):

    # t = turtle_name
    # n = accuracy = about30
    # l = length_of_leaf
    # a = thinness_of_leaf
    
    #go
    for i in range(n):
        t.fd(l)
        t.lt(a)

    #turn    
    turn =  180 - (a*n)
    t.lt(turn)

    #back
    for i in range(n):
        t.fd(l)
        t.lt(a)

    #turn
    t.lt(turn)

        
def draw_leafs(k):

    # k = number_of_leaf
    
    t = bob
    n = 30
    l = 5
    a = 0.5
    
    for i in range(k):
         draw_leaf(t, n, l, a)
         t.lt(360 / k)

draw_leafs(12)

