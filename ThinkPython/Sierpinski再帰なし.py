import rhinoscriptsyntax as rs
import math as ma

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def draw_triangle((x1,y1,z1), (x2,y2,z2), (x3,y3,z3)):
    """
    receives:
        (x1,y1,z1), (x2,y2,z2), (x3,y3,z3)  three points 
    works:
        draw the triangle based on the three points.
    returns:
        None
    """
    
    p1 = (x1, y1, z1)
    p2 = (x2, y2, z2)
    p3 = (x3, y3, z3)
    
    rs.AddLine(p1, p2)
    rs.AddLine(p1, p3)
    rs.AddLine(p2, p3)

def draw_Sierpinski(n):
    
    """
    receives:
        n   int n>=0. the number of recursions
    works:
        draw the sierpinski gasket
    returns:
        None
    """
    ax = -2
    ay = 0
    az = 0
    
    bx = 4
    by = 0
    bz = 0
    
    cx = 0
    cy = 3
    cz = 0
    
    a = (ax, ay, az)
    b = (bx, by, bz)
    c = (cx, cy, cz)
    
    #collect combination points coordinate
    
    box = []
    #box = [combination of the three points][id of the point][coordinate of the point]
    
    for i in range(0, n + 1):
        if i == 0:
            box.append((a, b, c))
        else:
            b = len(box) 
            
            for k in range(b - 3**(i-1), b):
                ax = box[k][0][0]
                ay = box[k][0][1]
                az = box[k][0][2]
                
                bx = box[k][1][0]
                by = box[k][1][1]
                bz = box[k][1][2]
                
                cx = box[k][2][0]
                cy = box[k][2][1]
                cz = box[k][2][2]
                
                a = (ax, ay, az)
                b = (bx, by, bz)
                c = (cx, cy, cz)
                
                new_ax = abs(bx-cx)/2 + min(bx, cx)
                new_ay = abs(by-cy)/2 + min(by, cy)
                new_az = abs(bz-cz)/2 + min(bz, cz)
                
                new_bx = abs(ax-cx)/2 + min(ax, cx)
                new_by = abs(ay-cy)/2 + min(ay, cy)
                new_bz = abs(az-cz)/2 + min(az, cz)
                
                new_cx = abs(ax-bx)/2 + min(ax, bx)
                new_cy = abs(ay-by)/2 + min(ay, by)
                new_cz = abs(az-bz)/2 + min(az, bz)
                
                new_a =(new_ax, new_ay, new_az)
                new_b =(new_bx, new_by, new_bz)
                new_c =(new_cx, new_cy, new_cz)
                
                box.append((a, new_b, new_c))
                box.append((new_a, new_b, c))
                box.append((new_a, b, new_c))
    
    #draw Sierpinski
    b = len(box)
    for i in range(0,b):
        draw_triangle(box[i][0],box[i][1],box[i][2])

delete_all()
draw_Sierpinski(6)