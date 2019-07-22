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

ran_1 = 3#rd.randint(1,10)
ran_2 = 2

def draw_bottom():
    points = []
    for theta in rs.frange(0,360,c):
        R = 0 #* ma.cos(ma.radians(theta))
        
        x = (R+15)* ma.cos(ma.radians(theta)) +5
        y = (R+15)* ma.sin(ma.radians(theta)) +5
        
        points.append((x,y,0))
    curve = rs.AddCurve(points)
    return curve

def draw_outline(z):
    db = draw_bottom()
    theta = z 
    xy = 1/ma.log(z)
    scale = rs.ScaleObject(db, (0, 0, z/3), (xy+0.5, xy+0.5, 0), True)
    curve = rs.RotateObject(scale, (0 ,0, z), z, False)
    rs.DeleteObject(db)
    return curve


def draw_sikaku(i):
    h = height = 10000
    r = radius = 10000
    theta = ma.radians(i)
    p1 = (0, 0, 0)
    p2 = (0, 0, h)
    path = rs.AddLine(p1,p2)
    side = rs.AddLine((0, 0, -3),(r*ma.cos(theta), r*ma.sin(theta), -3))
    plate = rs.ExtrudeCurve(side,path)
    rs.DeleteObject(path)
    rs.DeleteObject(side)
    return plate

def draw_arc(p,theta,k):
    #k=-1,1
    p1 = rs.AddPoint(p)
    p2 = rs.CopyObject(p1, polar(t,theta,0))
    p3 = rs.CopyObject(p1, polar(t/2,theta,0))
    p4 = rs.CopyObject(p3, (0,0,t/4*k))
    arc =rs.AddLine(p1,p2)
    return arc

def draw_rectangle_1((x, y, z), theta):
    t = 1
    p = (x, y, z)
    p0 = rs.AddPoint(p)
    p1 = rs.CopyObject(p0, polar(0.27, theta+45,0))
    p2 = rs.CopyObject(p0, polar(t, theta+169,0))
    p3 = rs.CopyObject(p0, polar(t, theta-169,0))
    p4 = rs.CopyObject(p0, polar(0.27, theta-45,0))
    rec = [ rs.AddLine(p1,p2),
            rs.AddLine(p2,p3),
            rs.AddLine(p3,p4),
            rs.AddLine(p4,p1)]
    return rec

def draw_rectangle_2(p,theta):
    t = 1
    p0 = rs.AddPoint(p)
    p1 = rs.CopyObject(p0, polar(t, theta+11,0))
    p2 = rs.CopyObject(p0, polar(t, theta+169,0))
    p3 = rs.CopyObject(p0, polar(t, theta-169,0))
    p4 = rs.CopyObject(p0, polar(t, theta-11,0))
    rec = [ rs.AddLine(p1,p2),
            rs.AddLine(p2,p3),
            rs.AddLine(p3,p4),
            rs.AddLine(p4,p1)]
    return rec


def draw_warp():
    
    n = 360
    warp = []
    for i in rs.frange(0, n, d):
        point = []
        for z in rs.frange(2, 50, 5):
            si = draw_sikaku(i)
            do = draw_outline(z)
            p = rs.CurveSurfaceIntersection(do, si)
            rs.DeleteObject(si)
            rs.DeleteObject(do)
            point.append(p[0][1])
        
        curve_1 = rs.AddCurve(point)
        curve_2 = rs.CopyObject(curve_1, polar(t, i, 0))
        
        domain = rs.CurveDomain(curve_1)
        increment = (domain[1]-domain[0])
        
        point_1 = rs.EvaluateCurve(curve_1, domain[0])
        point_2 = rs.EvaluateCurve(curve_1, domain[1])
        
        
        arc_1 = draw_arc(point_1, i, -1)
        arc_2 = draw_arc(point_2, i,  1)
        
        wakame = [curve_1, curve_2, arc_1, arc_2]
        
#        rs.RotateObjects(wakame,(0,0,0),90,polar(10,i,0),False)
#        rs.MoveObjects  (wakame, polar(0, i ,0))
#        rs.RotateObjects(wakame,(0,0,0),-i,None,False)        
#        rs.MoveObjects  (wakame, (i*t/3,10,5))
        
        point_3 = rs.EvaluateCurve(curve_1, increment*2/5.4)
        rec_1 = draw_rectangle_2(point_3, 0)        
        point_4 = rs.EvaluateCurve(curve_1, increment*1/7)
        rec_2 = draw_rectangle_2(point_4, 0)
        
        warp.append(curve_1)
    
    
    return warp


def draw_top_wakka():
    top_outline = draw_outline(20)
    rs.ScaleObject(top_outline,(0,0,20),(1.09,1.09,1),False)
    
    n = 360
    top_rectangle=[]
    for i in rs.frange(0, n, d):
        si = draw_sikaku(i)
        p = rs.CurveSurfaceIntersection(top_outline, si)
        rs.DeleteObject(si)
        dr = draw_rectangle_1(p[0][1], i)
        rs.MoveObject(dr,polar(0.1, i, 0))
        top_rectangle.append(dr)
        
    top_curve=[top_outline,
               top_rectangle]

def draw_bottom_wakka():
    bottom_outline  = draw_outline(11)
    rs.ScaleObject(bottom_outline,(0,0,10),(1.06,1.06,1),False)
    
    n=360
    bottom__rectangle = []
    for i in rs.frange(0, n, d):
        si = draw_sikaku(i)
        do = draw_outline(11)
        p = rs.CurveSurfaceIntersection(do, si)
        rs.DeleteObject(si)
        rs.DeleteObject(do)
        dr = draw_rectangle_1(p[0][1],i)
        rs.MoveObject(dr,polar(0.6, i, 0))
        bottom__rectangle.append(dr)
    


def draw_all():
    draw_warp()
    draw_top_wakka()
    draw_bottom_wakka()


delete_all()

t = thickness = 3
d = density_of_warp = 20 #(smaller is more density)
c =  constrictions = 10 #(360_no_yakusuu)(smaller is more dekoboko)

print ran_1

draw_all()

delete_something(1)
delete_something(8)