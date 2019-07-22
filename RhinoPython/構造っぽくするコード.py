import rhinoscriptsyntax as rs

a = 0.06 #kukan no futosa
b = 0.5  #haji no futosa
b0 = 1.5 #mannaka no hutosa
c = 0.2  #chotto sita zure

def periods_ofcurve( curve, n ):
    domain = rs.CurveDomain( curve )
    cpoint_list = [ ] 
    point0 = rs.EvaluateCurve( curve , domain[0] )
    point1 = rs.EvaluateCurve( curve , domain[1] )
    #rs.AddPoints( [ point0, point1 ] )
    for i in range(n+1):
        d = domain[1] * ( i )/ n
        point_lower = rs.EvaluateCurve( curve , d-a )
        point_upper = rs.EvaluateCurve( curve , d+a )
        cpoint_list.append( point_lower )
        cpoint_list.append( point_upper )
    return cpoint_list

def draw_grid( curve0 ,curve1, n ):
    d0 = periods_ofcurve( curve0, n )
    d1 = periods_ofcurve( curve1, n )
    curves_upper = []
    curves_lower = []
    
    for i in range(n+1): 
        point00 = d0[ 2*i + 1 ]
        point01 = d0[ 2*i + 0 ]
        point10 = d1[ 2*i + 1 ]
        point11 = d1[ 2*i + 0 ]
        if i==0:
            curve_upper = rs.AddCurve([point00, point10])
            #rs.AddCurve([point01, point11])
            curves_upper.append(curve_upper)
        elif i==n:
            #rs.AddCurve([point00, point10])
            curve_lower = rs.AddCurve([point11, point01])
            curves_lower.append(curve_lower)
        else:
            curve_upper = rs.AddCurve([point00, point10])
            curve_lower = rs.AddCurve([point11, point01])
            curves_upper.append(curve_upper)
            curves_lower.append(curve_lower)
    curves_all = [ curves_upper, curves_lower ]
    return curves_all

def draw_hole( grid00, grid01 ):
    grids = [ grid00, grid01 ]
    points = []
    lists = []
    for i in grids:
        domain = rs.CurveDomain(i)
        domains = [ domain[0]+b, domain[1]-b0*b, domain[1]-b ]
        lists.append( domains )
        for ii in domains:
            point = rs.EvaluateCurve( i, ii ) 
            points.append( point )
    for i in range(2):
        grid = rs.AddCurve( [ points[i*3], points[5-i*3] ] )
        domain0 = rs.CurveDomain( grid )
        domain1 = domain0[1] - c
        point = rs.EvaluateCurve( grid, domain1 )
        #rs.AddPoint(point)
        rs.AddCurve( [ point, points[i*3+1] ] )
        rs.TrimCurve( grids[i], ( lists[i][0], lists[i][1] ) )
        rs.TrimCurve( grid, ( domain0[0], domain1 ) )

def draw_holes( curve0, curve1, n):
    grids = draw_grid( curve0, curve1, n )
    for i in range(n):
        draw_hole( grids[0][i], grids[1][i] )

def draw_severaltimes( n ):
    x = 1
    circle = rs.AddCircle( ( 0, 0, 0 ), 10 )
    rs.ObjectColor( circle, ( 255, 0, 0 ),  )
    while x == 1:
        curve0 = rs.GetObject("Select a curve(If you want program to finish, click red circle) ")
        if curve0 == circle:
            rs.DeleteObject( circle )
            break
        else:
            curve1 = rs.GetObject("Select a curve")
            draw_holes( curve0, curve1, n )

draw_severaltimes(15)