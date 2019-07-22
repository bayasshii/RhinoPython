import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(n):
    something = rs.ObjectsByType(n)
    rs.DeleteObjects(something)

def polar(r,theta):
    x = r * ma.cos(ma.radians(theta))
    y = r * ma.sin(ma.radians(theta))
    return (x,y,0)

def komatsu_moyou():
    R = 360
    r = 10
    t1 = 5
    t2 = 18
    
    all_points = []
    for a in rs.frange(1, r, r/t1):
        points = []
        for b in rs.frange(0, R, R/t2):
            radius = a
            theta = b
            p = polar(a,b)
            points.append(p)
        all_points.append(points)
    print all_points
    
    for c in range(0,t1):
        for d in range(0,t2+1):
            p1 = all_points[c][d]
            p1p = rs.AddPoint(p1)
            
            p2 = all_points[c][d-1]
            p2p = rs.AddPoint(p2)
            
           # rs.AddLine(p1, p2)
            
            p3 = all_points[c-1][d]
            p3p = rs.AddPoint(p3)
            
            p4 = all_points[c-1][d-1]
            p4p = rs.AddPoint(p4)
            
           # rs.AddLine(p3, p2)
            
            (x1, y1, z1) = rs.PointCoordinates(p1p)
            (x2, y2, z2) = rs.PointCoordinates(p2p)
            (x3, y3, z3) = rs.PointCoordinates(p3p)
            (x4, y4, z4) = rs.PointCoordinates(p4p)
            
            x = (x1+x2+x3+x4)/4 + rd.random()/3
            y = (y1+y2+y3+y4)/4 + rd.random()/3
            p = rs.AddPoint(x, y, 0)
            
            rs.AddLine(p,p1)
            rs.AddLine(p,p2)
            rs.AddLine(p,p3)
            rs.AddLine(p,p4)
    
#    for e in range(0,t2):
#        p1 = all_points[0][e]
#        p2 = all_points[0][e+1]
#        rs.AddLine(p1,p2)
#        p3 = all_points[t1-1][e]
#        p4 = all_points[t1-1][e+1]
#        rs.AddLine(p3,p4)


delete_all()

komatsu_moyou()

delete_something(1)