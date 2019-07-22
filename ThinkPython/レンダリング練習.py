import rhinoscriptsyntax as rs
import math as ma
import random as rd


def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(k):
    some_objects = rs.ObjectsByType(k)
    rs.DeleteObjects(some_objects)

delete_all()

def a():
    a = (1,0,0)
    b = (5,0,5)
    c = (2,0,10)
    d = (10,0,15)
    curve = rs.AddCurve((a,b,c,d),5)
    axis = ((0,0,0),(0,0,10))
    rs.AddRevSrf(curve,axis,0,360)
    rs.AddSphere((0,0,12),3)

def b():
    c1 = rs.AddCircle((0,0,0),5)
    c2 = rs.AddCircle((0,5,5),3)
    c3 = rs.AddCircle((3,3,10),5)
    rs.AddLoftSrf((c1,c2,c3),None,None,1)

def c():
    a = rs.AddLine((0,0,0),(0,0,1))
    p = []
    r = 10
    for k in range(0,50):
        t = (k*ma.sin((k*r)/(2*ma.pi)),k*ma.cos((k*r)/(2*ma.pi)),0)
        p.append(t)
    b = rs.AddCurve(p,5)
    rs.ExtrudeCurve(a,b)

#good
def d(t, n):
    """
    receives:
         t = theta syuuki of sin  (0 < t < 90)
         n = number of waves  (0 < n < 50)
    works:
        draw waves
    returns:
        None
    """ 
    for x in range(0, n):
        points = []
        for y in range(1, n):
            p = (x, y, ma.sin((ma.radians(t*(y+x)))))
            points.append(p)
            #rs.AddPoint(p)
        a = rs.AddCurve(points, 5)
        b = rs.AddLine((x, 0, 0), (x+0.7, 0, 0))
        rs.ExtrudeCurve(a, b)
        
    for y in range(1,n):
        list = []
        for x in range(0,n):
            p = (x, y,  ma.cos(ma.radians(t*(x+y))))
            list.append(p)
        a = rs.AddCurve(list, 5)
        b = rs.AddLine((0, y, 0), (0, y+0.7, 0))
        rs.ExtrudeCurve(a, b)
#d(30,30)
#good
def dd(t, n):
    """
    receives:
         t = theta syuuki of sin  (0 < t < 90)
         n = number of waves  (0 < n < 200)
    works:
        draw waves
    returns:
        None
    """ 
    list = []
    for x in range(0, n):
        for y in range(0, n):
            p = [x, y, 0]
            list.append(p)
    
    number =  len(list)
    
    rx = rd.random()*n
    ry = rd.random()*n
    nn = n/2
    
    for k in range(0, number) :
        x = list[k][0]
        y = list[k][1]
        dx = x - rx
        dy = y - ry
        d = ma.sqrt(dx**2 + dy**2)
        
        if d < nn:
            list[k][2] = list[k][2] + ((nn-d)/6)*ma.sin(ma.radians(d*10))
        else:
            pass
    
    rx = rd.random()*n
    ry = rd.random()*n
    for k in range(0, number) :
        x = list[k][0]
        y = list[k][1]
        dx = x - rx
        dy = y - ry
        d = ma.sqrt(dx**2 + dy**2)
        
        if d < nn:
            list[k][2] = list[k][2] + (nn-d)/3*ma.cos(ma.radians(d*3))
        else:
            None
    rx = rd.random()*n
    ry = rd.random()*n
    for k in range(0, number) :
        x = list[k][0]
        y = list[k][1]
        dx = x - rx
        dy = y - ry
        d = ma.sqrt(dx**2 + dy**2)
        
        if d < nn:
            list[k][2] = list[k][2] + (nn-d)/10
        else:
            None
    for i in range(0,n):
        a = rs.AddCurve(list[i*n:(i+1)*n], 5)
        b = rs.AddLine((x, 0, 0), (x+0.7, 0, 0))
        rs.ExtrudeCurve(a, b)
#dd(50,100)
#good
def e(theta, num):
    """
    receives:
        theta = degree of line ( 0 < theta < 45 ) 
        num = number of pattern ( 0 < num < 15 )
    works:
        draw tile pattern
    returns:
        None
    """
    def base(x,y):
        d = ma.radians(theta) 
        
        r = 1/ma.cos(d) - (ma.sin(d)**2)/ma.cos(d)
        n = r * ma.sin(d)
        k = r * ma.cos(d)
        
        a1 = (x    ,     y, 0)
        b1 = (x    , y + 1, 0)
        c1 = (x + 1, y + 1, 0)
        d1 = (x + 1,     y, 0)
        
        a2 = (    x + k,     y + n, 0)
        b2 = (    x + n, y + 1 - k, 0)
        c2 = (x + 1 - k, y + 1 - n, 0)
        d2 = (x + 1 - n,     y + k, 0)
        
        l1 = rs.AddLine(a1, a2)
        l2 = rs.AddLine(b1, b2)
        l3 = rs.AddLine(c1, c2)
        l4 = rs.AddLine(d1, d2)
    
    for i in range(0,num):
       for k in range(0,num):
           base(i,k) 
    
    line = rs.ObjectsByType(0)
    n = len(line)
    for i in range(0,n):
        a = line[i]
        b = rs.AddLine((0, 0, 0), (0, 0, 0.05))
        c = rs.RotateObject(b, (0,0,0), 90, None, False)
        s = rs.ExtrudeCurve(a, b)
        rs.ExtrudeSurface(s, c)
e(30,10)
#good
def f(r,k):
    """
    receives:
        r = the size of all rectangles ( 50<r )
        k = the density of rectangles (2<k)
        
    works:
        draw cube
    returns:
        None
    """
    def cube(x,y,z):
        line1 = rs.AddLine((x, y, z),(  x, y+5, z))
        line2 = rs.AddLine((x, y, z),(x+5,   y, z))
        surface = rs.ExtrudeCurve(line1,line2)
        line3 = rs.AddLine((x,y,0),(x,y,5))
        rs.ExtrudeSurface(surface, line3)
    for x in rs.frange(0, r , 6):
        for y in rs.frange(0, r, 6):
            for z in rs.frange(0, r, 6):
                if rd.random() * z  < k:
                    cube(x,y,z)
                else:
                    None
#f(100,10)
#Failure
def g():
    """
    receives:
        theta = degree of line ( 0 < theta < 45 ) 
        num = number of pattern ( 0 < num < 15 )
    works:
        draw wire
    returns:
        None
    """
    r =10
    sp = rs.AddSphere((0,0,0),r)
    box = []
    for x in rs.frange(-r,r,0.1):
       for y in rs.frange(-r,r,0.1):
            if r**2 > x**2 + y**2:
                z = ma.sqrt(abs(r**2 - x**2 - y**2) )
                box.append((x,y,z))
       for y in rs.frange(-r,r,0.1):
            if r**2 > x**2 + y**2:
                z = ma.sqrt(abs(r**2 - x**2 - y**2) )
                box.append((x,-y,-z))
    ll = len(box)
    rbox=[]
    for i in range(0,ll):
        r = rd.random()
        if r < 0.01:
            rbox.append(box[i])
    
    box2 = []
    box2.append(rd.sample(box,300))
    
    box3=[]
    """
    for i in range(0,100):
        if i == 0:
            dis=[]
            dis2=[]
            for k in range(1,100):
                x =  box2[0][0][0]
                y =  box2[0][0][1]
                z =  box2[0][0][2]
                xx = box2[0][k][0]
                yy = box2[0][k][1]
                zz = box2[0][k][2]
                d = (x-xx)**2 + (y-yy)*2 + (z-zz)**2
                dis.append(d)
                dis2.append(d)
            box2.remove(box2[0][0])
            dis.sort()
            n = dis2.index(dis[-1])
            k = box2[n]
            box2.remove(k)
    """
    curve = rs.AddCurve(rbox,2)
    rs.AddPipe(curve,0,0.05,True)
g()
#delete_something(4)

