import rhinoscriptsyntax as rs
import math as ma

def draw_triangle((x1,y1,z1), (x2,y2,z2), (x3,y3,z3)):
    """
    receives:
        (x1,y1,z1), (x2,y2,z2), (x3,y3,z3)  three point coordinate
    works:
        draw the triangle that locates at the center
    returns:
        None
    """
    
    p1x = (x1+x2)/2
    p1y = (y1+y2)/2
    p2x = (x1+x3)/2
    p2y = (y1+y3)/2
    p3x = (x2+x3)/2
    p3y = (y2+y3)/2
    
    p1 = (p1x, p1y, 0)
    p2 = (p2x, p2y, 0)
    p3 = (p3x, p3y, 0)
    
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
    bx = 4
    cy = 3
    
    a = (0, 0, 0)
    b = (bx, 0, 0)
    c = (0, cy, 0)
    
    rs.AddLine(a, b)
    rs.AddLine(c, a)
    rs.AddLine(b, c)
    
    
    if n < 0:
        print ('n must not be negative')
    elif n == 0:
        draw_triangle(a, b, c)
        return ((a, b, c))
    else:
        draw_Sierpinski(n-1)
        draw_triangle(a, b, c)
        
        draw_Sierpinski(n-1)
        cy = cy/2
        draw_triangle(a, b, c)
        
        draw_Sierpinski(n-1)
        bx = bx/2
        cy = cy/2
        draw_triangle(a, b, c)

draw_Sierpinski(3)