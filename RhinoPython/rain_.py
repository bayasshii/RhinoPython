import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(n):
    something = rs.ObjectsByType(n)
    rs.DeleteObjects(something)

def polar_to_rectangular(r,theta):
    x = r * ma.cos(theta)
    y = r * ma.sin(theta)
    return (x, y, 0)

def draw_tree():
    x_coordinate = []
    y_coordinate = []
    r = 2
    ran = 10
    n = 100
    for a in range(0, n):
        if a == 0 :
            x = rd.uniform(-1, 1) * ran
            rs.AddCircle((x, r, 0), r)
            x_coordinate.append(x)
            y_coordinate.append(r)
            
        else:
            maxx = max(x_coordinate)
            minn = min(x_coordinate)
            x = rd.uniform(minn, maxx) + rd.uniform(-1, 1) * ran 
            
            y_contact = []
            x_contact = []
            y_contacted = []
            x_contacted = []
            
            b = len(x_coordinate) -1
            
            while (b != -1):
                if x_coordinate[b] - r*3 <= x <= x_coordinate[b] + r*3:
                    y = ma.sqrt((r*3)**2 - (x_coordinate[b] - x)**2) + y_coordinate[b] 
                    
                    y_contact.append(y)
                    x_contact.append(x)
                    y_contacted.append(y_coordinate[b])
                    x_contacted.append(x_coordinate[b])
                    b -= 1
                    
                else:
                    b -= 1
            else :
                if 1 <= len(y_contact) :
                    y_real = max(y_contact)
                    number = y_contact.index(y_real)
                    x_real = x_contact[number]
                    
                    y_coordinate.append(y_real)
                    x_coordinate.append(x_real)
                    
                    d =( (x_real - x_contacted[number])*1/3 + x_contacted[number], (y_real - y_contacted[number])*1/3 + y_contacted[number], 0)
                    e =( (x_real - x_contacted[number])*2/3 + x_contacted[number], (y_real - y_contacted[number])*2/3 + y_contacted[number], 0)
                    rs.AddLine(d, e)
                    rs.AddCircle((x_real, y_real, 0), r)
                else:
                    rs.AddCircle((x, r, 0), r)
                    x_coordinate.append(x)
                    y_coordinate.append(r)

delete_all()
draw_tree()