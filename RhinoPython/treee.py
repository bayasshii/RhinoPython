import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(n):
    something = rs.ObjectsByType(n)
    rs.DeleteObjects(something)

def draw_tree():
    x_coordinate = []
    y_coordinate = []
    r = 2
    R = 100
    n = 1000
    for a in range(0, n):
        if a == 0 :
            x = rd.uniform(-1, 1)*R 
            rs.AddCircle((x, r, 0), r)
            x_coordinate.append(x)
            y_coordinate.append(r)
        else:
            x = rd.uniform(-1, 1) * R 
            b = len(x_coordinate) -1
            y_contact = []
            while (b != -1):
                if x_coordinate[b] - r*2 <= x <= x_coordinate[b] + r*2:
                    y = ma.sqrt((r*2)**2 - (x_coordinate[b] - x)**2) + y_coordinate[b] 
                    y_contact.append(y)
                    b -= 1
                else:
                    b -= 1
            else :
                if 1 <= len(y_contact) :
                    c = max(y_contact) 
                    x_coordinate.append(x)
                    y_coordinate.append(c)
                    rs.AddCircle((x, c, 0), r)
                else:
                    rs.AddCircle((x, r, 0), r)
                    x_coordinate.append(x)
                    y_coordinate.append(r)

delete_all()
draw_tree()