import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def look_for_firefly(nod):
    
    firefly = []
    
    for k in range(1, nod):
        r1 = rd.random()
        r2 = rd.random()
        r3 = rd.random()
        (x, y) = ((5 * r1),(5 * r2)) #zahyou
        light = 5 * r3 #hotaru_no_hikari
        firefly.append((light, (x,y)))
    
    for l in range(1,10):
        for k in range(1,nod):
            for n in range(1, nod):
                if firefly[k][0] > firefly[n][0]:
                    h = (firefly[k][0]/25)**2
                    firefly[n][1] = firefly[n][1]+ h*(firefly[k][1])
    for a in range(1, nod):
        rs.AddCircle(firefly[a][1],0.1)

look_for_firefly(50)