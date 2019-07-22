import rhinoscriptsyntax as rs
import math as ma
import random as rd


def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_all_points():
    all_points = rs.ObjectsByType(1)
    rs.DeleteObjects(all_points)


def cog(a,b,c): 
    (a1, a2, a3) = rs.PointCoordinates(a)
    (b1, b2, b3) = rs.PointCoordinates(b)
    (c1, c2, c3) = rs.PointCoordinates(c)
    
    center_of_gravity = rs.AddPoint((a1+b1+c1)/3, (a2+b2+c2)/3, (a3+b3+c3)/3)
    return center_of_gravity

#'l' and 'r' are points

def bottom_line(l, r):
    bottom_line = rs.AddLine(l, r)
    return bottom_line

def left_line(l, r):
    left_line = rs.RotateObject(bottom_line(l, r), l,  60, None, True)
    return left_line

def right_line(l, r):
    right_line = rs.RotateObject(bottom_line(l, r), r, -60, None, True)
    return right_line

def triangle(l, r):
    triangle = [bottom_line(l, r),
                left_line(l, r),
                right_line(l, r)]
    return triangle

def cut_triangle(tri):
    rs.ObjectColor(tri,colors[0])
    return tri

def tri_tri(s):
    #pxx = point
    #cxx = cordinate
    
    p01 = rs.AddPoint(-s, -s*ma.sqrt(3), 0)
    p02 = rs.AddPoint( s, -s*ma.sqrt(3), 0)
    
    #tri_1
    c01   = rs.PointCoordinates(p01)
    c02   = rs.PointCoordinates(p02)
    tri_1 = triangle(c01, c02)
    
    #tri_2
    tri_2 = triangle(c02, c01)
    
    #tri_3
    p03   = rs.RotateObject(p02, c01, -60, None, False)
    c03   = rs.PointCoordinates(p03)
    tri_3 = triangle(c03, c01)
    
    #tri_4
    p04   = rs.RotateObject(p03, c01, -60, None, False)
    c04   = rs.PointCoordinates(p04)
    tri_4 = triangle(c04, c01)
    
    #tri_5
    p05   = rs.RotateObject(p04, c01, -60, None, False)
    c05   = rs.PointCoordinates(p05)
    tri_5 = triangle(c04,c05)
    
    #tri_6
    p06   = rs.RotateObject(p01, c05, -120, None, False)
    c06   = rs.PointCoordinates(p06)
    tri_6 = triangle(c06, c05)
    
    #tri_7
    p07   = rs.RotateObject(p06, c05 , -60, None, False)
    c07   = rs.PointCoordinates(p07)
    tri_7 = triangle(c07, c05)
    
    #tri_8
    p08   = rs.RotateObject(p07, c05, -60, None, False)
    c08   = rs.PointCoordinates(p08)
    tri_8 = triangle(c07, c08)
    
    #tri_9
    p09   = rs.RotateObject(p05, c08, -120, None, False)
    c09   = rs.PointCoordinates(p09)
    tri_9 = triangle(c09, c08)
    
    
    pp00 = rs.AddPoint(0,0,0)
    pp01 = rs.AddPoint(c01)
    pp02 = rs.AddPoint(c02)
    pp03 = rs.AddPoint(c03)
    pp04 = rs.AddPoint(c04)
    pp05 = rs.AddPoint(c05)
    pp06 = rs.AddPoint(c06)
    pp07 = rs.AddPoint(c07)
    pp08 = rs.AddPoint(c08)
    pp09 = rs.AddPoint(c09)
    
    matrix = [[tri_1, cog(pp00, pp01, pp02)],
              [tri_2, cog(pp01, pp02, pp03)],
              [tri_3, cog(pp02, pp03, pp04)],
              [tri_4, cog(pp03, pp04, pp05)],
              [tri_5, cog(pp04, pp05, pp06)],
              [tri_6, cog(pp05, pp06, pp07)],
              [tri_7, cog(pp06, pp07, pp08)],
              [tri_8, cog(pp07, pp08, pp09)],
              [tri_9, cog(pp08, pp09, pp09)]]
    
    
    #make_numbers_for_selecting_matrix
    
    r = rd.random()
    print r
    
    if r <= 0.50:  #funky
        rd_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        n = rd.sample(rd_list, 2)
        k = rd.sample(rd_list, 2)
        print n
        print k
    if 0.50 < r <= 0.90: #tidy
        rd_list = [[1,0], [2,1], [3,2], [4,3], [5,4], [6,5], [7,6], [8,7]]
        n = rd.choice(rd_list)
        k = rd.choice(rd_list)
        print n
        print k
    else: #unexpected
        #cog_of_three_cogs
        rd_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        ul_1 = unexpected_list_1 = rd.sample(rd_list, 3)
        ul_2 = unexpected_list_2 = rd.sample(rd_list, 3)
        ul_3 = unexpected_list_3 = rd.choice(rd_list)
        ul_4 = unexpected_list_4 = rd.choice(rd_list)
        
        [a1, b1, c1]=[matrix[ul_1[0]][1], matrix[ul_1[1]][1], matrix[ul_1[2]][1]]
        [a2, b2, c2]=[matrix[ul_2[0]][1], matrix[ul_2[1]][1], matrix[ul_2[2]][1]]
        
        matrix.append([matrix[ul_3][0], cog(a1, b1, c1)])
        matrix.append([matrix[ul_4][0], cog(a2, b2, c2)])
        n = [-1, -1]
        k = [-2, -2]
    
    
    #draw_many_tri
    ##n=[1,0]= appear_star_at_center
    
    f = from_ =0.01
    t = to    =0.99
    b = by    =0.10
    
    #variable
    for s in rs.frange(f, t, b):
        rs.ScaleObject(matrix[n[0]][0], matrix[n[1]][1],(s, s, 0), True)
    
    #variable
    for s in rs.frange(f, t, b):
        rs.ScaleObject(matrix[k[0]][0], matrix[k[1]][1],(s, s, 0), True)
    
    #fixed_tris
    for s in rs.frange(f, t, b):
        rs.ScaleObject(tri_2, cog(pp01, pp02, pp03),(s, s, 0), True)
    for s in rs.frange(f, t, b):    
        rs.ScaleObject(tri_6, cog(pp05, pp06, pp07),(s, s, 0), True)
    
    #sometimes_cut_triangle
    s_c = rd.random()
    if s_c <= 0.3:
         cut_list = [0, 2, 3, 4, 6, 7, 8]
         c = rd.choice(cut_list)
         print c
         c_tri = matrix[c][0]
         cut_triangle(c_tri)
    else:
        None
    
    all_tri = rs.ObjectsByType(0)
    return all_tri

def rotate_triangles(s):
    t = tri_tri(s)
    for r in rs.frange(0,300,60):
        rs.RotateObject(t, (0, 0, 0), r, None, True)

def outline(s):
    
    x1= 6*s
    y1= 0 
    x2= 3*s
    y2= 6*s*ma.sqrt(3)/2
    
    xy1 = (x1, y1, 0)
    xy2 = (x2, y2, 0)
    
    line_origin = rs.AddLine(xy1, xy2)
    
    o = length_of_outline = 0.1 #0.05<0<0.10  
    line = rs.ScaleObject(line_origin, (0, 0, 0), (1+o, 1+o, 0), False)
    
    for angle in rs.frange(60, 360, 60):
        rs.RotateObject(line, (0, 0, 0), angle, None, True)
    
    all_lines = rs.ObjectsByType(0)
    
    rs.ObjectColor(all_lines,colors[0])

colors  = [(255, 0, 0)] 

delete_all()

s = size_of_one_tri = 5
#2*s = length_of_one_side

#outline(s)
#rotate_triangles(s)

#delete_all_points()

delete_all_points()