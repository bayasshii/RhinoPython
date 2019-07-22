import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(n):
    something = rs.ObjectsByType(n)
    rs.DeleteObjects(something)

def polar(r, theta):
    x = r * ma.cos(theta)
    y = r * ma.sin(theta)
    return (x, y, 0)

def noise_circle((xx, yy, zz), R):
    point = []
    for t in rs.frange(0, 360, 20):
        ranran = rd.randint(4, 8)
        ranranran = rd.random()/ranran + 0.3
        sin = ma.sin(ma.radians(t/5 + 54))/2
        R_real = ( ranranran + sin ) * R 
        
        ran = rd.randint(1, 2)
        
        p = rs.AddPoint(xx, yy, zz)
        rs.MoveObject(p, polar(R_real, ma.radians(t)))
        
        point.append(p)
    point.append(point[0])
    c = rs.AddCurve(point)
    ran = rd.randint(1, 90)
    rs.RotateObject(c, (xx, yy, zz), ran, None, False)

def draw_stone():
    r_box     = []
    theta_box = []
    R_box     = []
    
    #how many circles
    n = 100
    
    for a in range(0, n):
        if a == 0 :
            #center big circle
            R = 20
            noise_circle(polar(0,0), R)
            
            theta_box.append(0)
            r_box.append(0)
            R_box.append(R)
        else:
            #probability to make big circle is1/7 
            random = rd.randint(1,7)
            
            if random == 1:
                #big circle size
                max_circle = 15
                min_circle = 10
                R = rd.randint(min_circle, max_circle)
            else:
                #normal circle size
                max_circle = 8
                min_circle = 3
                R = rd.randint(min_circle, max_circle) 
            
            angle = []
            for t in rs.frange(1,360,72):
                angle.append(t)
            theta = rd.choice(angle) + rd.randint(-5, +5)
            
            r_contact       = []
            r_contacted     = []
            theta_contact   = []
            theta_contacted = []
            R_contact       = []
            R_contacted     = []
            
            L = R*0.5
            
            b = 0
            #determine contact or not contact
            while (b != a):
                D = -(r_box[b] * ma.sin(theta_box[b] - theta))**2 + (R + L/2 + R_box[b])**2
                #if contact
                if D  > 0 :
                    r = (r_box[b]) * ma.cos(theta - theta_box[b]) + ma.sqrt(D)                   
                    if r > R_box[b]:
                        theta_contact.append(theta)
                        r_contact.append(r)
                        R_contact.append(R)
                        
                        theta_contacted.append(theta_box[b])
                        r_contacted.append(r_box[b])
                        R_contacted.append(R_box[b])
                        
                        b += 1
                    else:
                        b += 1
               #if not contact
                else:
                    b += 1
            
            else :
                #if we have contacted circle
                if 1 <= len(r_contact) :
                    r_real   = max(r_contact)
                    number   = r_contact.index(r_real)
                    r_before = r_contacted[number]
                    
                    theta_real   = theta_contact[number]
                    theta_before = theta_contacted[number]
                    
                    R_real   = R_contact[number]
                    R_before = R_contacted[number]
                    
                    noise_circle(polar(r_real, theta_real), R_real)
                    
                    #line ga aruto wakariyasui
                    #p_before = polar(r_before , theta_before)
                    #p_real = polar(r_real , theta_real)
                    #line1 = rs.AddLine(p_before, p_real)
                    
                    r_box.append(r_real)
                    theta_box.append(theta_real)
                    R_box.append(R_real)
                #if do not have
                else:
                    noise_circle(polar(R_box[0] + R + L, theta), R)
                    
                    theta_box.append(theta)
                    r_box.append(R + L + R_box[0])
                    R_box.append(R)

delete_all()

draw_stone()
delete_something(1)