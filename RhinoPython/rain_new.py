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
    R_box = []
    ran = 20
    n = 1000
    for a in range(0, n):
        if a == 0 :
            x = rd.uniform(-1, 1) * ran
            R = rd.randint(1,5)
            rs.AddCircle((x, R, 0), R)
            x_coordinate.append(x)
            y_coordinate.append(R)
            R_box.append(R)
        else:
            maxx = max(x_coordinate)
            minn = min(x_coordinate)
            x = rd.uniform(minn - ran, maxx + ran)  
            R = rd.randint(1,5)
            
            y_contact = []
            x_contact = []
            y_contacted = []
            x_contacted = []
            R_contact = []
            R_contacted = []
            
            b = len(x_coordinate) -1
            
            while (b != -1):
                if x_coordinate[b] - R_box[b] - R*2 < x < x_coordinate[b] + R_box[b] + R*2 :
                    
                    y = ma.sqrt(( R_box[b] + R*2 )**2 - (x_coordinate[b] - x)**2) + y_coordinate[b] 
                    
                    y_contact.append(y)
                    x_contact.append(x)
                    R_contact.append(R)
                    
                    y_contacted.append(y_coordinate[b])
                    x_contacted.append(x_coordinate[b])
                    R_contacted.append(R_box[b])
                    
                    b -= 1
                    
                else:
                    b -= 1
            else :
                if 1 <= len(y_contact) :
                    y_real   = max(y_contact)
                    number   = y_contact.index(y_real)
                    y_before = y_contacted[number]
                    
                    x_real   = x_contact[number]
                    x_before = x_contacted[number]
                    
                    R_real   = R_contact[number]
                    R_before = R_contacted[number]
                    
                    p1x = (x_real - x_before)* (R_before             / (R_real*2 + R_before)) + x_before
                    p1y = (y_real - y_before)* (R_before             / (R_real*2 + R_before)) + y_before
                    p2x = (x_real - x_before)* ((R_real + R_before)  / (R_real*2 + R_before)) + x_before
                    p2y = (y_real - y_before)* ((R_real + R_before)  / (R_real*2 + R_before)) + y_before
                    p1 = (p1x, p1y, 0)
                    p2 = (p2x, p2y, 0)
                    rs.AddLine(p1, p2)
                    
                    rs.AddCircle((x_real, y_real, 0), R_real)
                    
                    y_coordinate.append(y_real)
                    x_coordinate.append(x_real)
                    R_box.append(R)
                    
                else:
                    rs.AddCircle((x, R, 0), R)
                    x_coordinate.append(x)
                    y_coordinate.append(R)
                    R_box.append(R)

delete_all()
draw_tree()