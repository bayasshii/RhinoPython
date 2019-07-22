import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(n):
    something = rs.ObjectsByType(n)
    rs.DeleteObjects(something)

def polar(r, theta, h):
    x = r * ma.cos(ma.radians(theta))
    y = r * ma.sin(ma.radians(theta))
    z = h
    return (x,y,z)

def draw_sikaku(h):
    p1 = (1000, 1000, h)
    p2 = (1000, -1000, h)
    p3 = (1000, 0, h)
    p4 = (-1000, 0, h)
    path = rs.AddLine(p1,p2)
    side = rs.AddLine(p3,p4)
    plate = rs.ExtrudeCurve(path,side)
    rs.DeleteObject(path)
    rs.DeleteObject(side)
    return plate

def draw_rectangle1((x, y, z), theta):
    t = 1
    p = (x, y, z)
    p0 = rs.AddPoint(p)
    p1 = rs.CopyObject(p0, polar(0.115, theta+90,0))
    p2 = rs.CopyObject(p0, polar(0.115, theta-90,0))
    p3 = rs.CopyObject(p2, polar(1.0, theta,0))
    p4 = rs.CopyObject(p1, polar(1.0, theta,0))
    rec = [ rs.AddLine(p1,p2),
            rs.AddLine(p2,p3),
            rs.AddLine(p3,p4),
            rs.AddLine(p4,p1)]
    rs.MoveObject(rec, polar(0.4, theta, 0))
    rect = rs.RotateObjects(rec ,(0, 0, z), 90,(x,y,0), True)
    rect = rs.MoveObjects(rect,polar(-1, theta, 0))
    return rect

def wakame():
    h1 = 3
    h2 = 6
    p1_box = []
    p2_box = []
    for t in rs.frange(0, 360, 10):
        rg = ma.sin(ma.radians(t/3 + 30))/2 + 1.3
        hg = ma.sin(ma.radians(t/2))/4 + 0.5
        tt = 0.7
        
        r_1 =  5 
        theta_1 = t
        h_1 = 0
        p_1 = polar(r_1, theta_1 , h_1)
        
        r_2 =  6 
        theta_2 = t
        h_2 = 11 * hg
        p_2 = polar(r_2, theta_2 , h_2)
        
        r_3 =  10 *rg
        theta_3 = t
        h_3 = 15 * hg
        p_3 = polar(r_3, theta_3 , h_3)
        
        r_4 =  15 *rg
        theta_4 = t
        h_4 = 15 *hg
        p_4 = polar(r_4, theta_4 , h_4)
        
        r_5 =  5  + tt
        theta_5 = t
        h_5 = 0
        p_5 = polar(r_5, theta_5 , h_5)
        
        r_6 =  6  +tt
        theta_6 = t
        h_6 = 11 * hg -tt
        p_6 = polar(r_6, theta_6 , h_6)
        
        r_7 =  10 *rg +tt
        theta_7 = t
        h_7 = 15 * hg -tt
        p_7 = polar(r_7, theta_7 , h_7)
        
        r_8 =  15 *rg
        theta_8 = t
        h_8 = 15 *hg -tt
        p_8 = polar(r_8, theta_8 , h_8)
        
        p_1_box = [p_1, p_2, p_3, p_4]
        cu1 = rs.AddCurve(p_1_box)
        
        p_2_box = [p_5, p_6, p_7, p_8]
        cu2 = rs.AddCurve(p_2_box)
        
        l1 = rs.AddLine(p_1, p_5)
        l2 = rs.AddLine(p_4, p_8)
        
        si = draw_sikaku(h1)
        p1 = rs.CurveSurfaceIntersection(cu1, si)
        p1_box.append(p1[0][1])
        
        si = draw_sikaku(h2)
        p2 = rs.CurveSurfaceIntersection(cu1, si)
        p2_box.append(p2[0][1])
        
        r1 = draw_rectangle1(p1[0][1], t)
        r2 = draw_rectangle1(p2[0][1], t)
        
        rs.RotateObjects(r1,(0,0,0), 90, polar(12,t,0),False)
        rs.MoveObjects  (r1, polar(0, t ,0))
        rs.RotateObjects(r1,(0,0,0),-t,None,False)        
        rs.MoveObjects  (r1, (t*0.12,t*0.12,0))
        
        rs.RotateObjects(r2,(0,0,0), 90, polar(12,t,0),False)
        rs.MoveObjects  (r2, polar(0, t ,0))
        rs.RotateObjects(r2,(0,0,0),-t,None,False)        
        rs.MoveObjects  (r2, (t*0.12,t*0.12,0))
        
        all =[l1, l2, cu1, cu2]
        rs.RotateObjects(all,(0,0,0), 90, polar(12,t,0),False)
        rs.MoveObjects  (all, polar(0, t ,0))
        rs.RotateObjects(all,(0,0,0),-t,None,False)        
        rs.MoveObjects  (all, (t*0.12,t*0.12,0))
        
    c1 = rs.AddInterpCurve(p1_box)
    c2 = rs.AddInterpCurve(p2_box)
    
    rs.ScaleObject(c1, (0,0,h1), (1.2,1.2,1),True)
    rs.ScaleObject(c2, (0,0,h2), (1.1,1.1,1),True)
    rs.ScaleObject(c1, (0,0,h1), (0.6,0.6,0.75),True)
    rs.ScaleObject(c2, (0,0,h2), (0.9,0.9,1),True)
    rs.DeleteObject(c1)
    rs.DeleteObject(c2)
    
    all = [cu1,cu2]
    return all

delete_all()

wakame()
delete_something(1)
delete_something(8)