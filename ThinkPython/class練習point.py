import math as ma

class point(object):
    """Represents a point in 2D-space"""
    def __int__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "%2d,%2d"%(self.x,self.y)


    def __add__(self, other):
        if isinstance(self, point) and isinstance(other, point):
            return(self.add_point(other))
        else:
            return(self.increment(other))

    def add_point(self, other):
        p = point()
        p.x = self.x + other.x
        p.y = self.y + other.y
        return(p)

    def increment(self, t):
        p = point()
        p.x = self.x + t[0]
        p.y = self.y + t[1]
        return(p)
        

pp=point()
pp.x=2.0
pp.y=5.0


blank1 = point()
blank1.x = 3.0
blank1.y = 4.0

blank2 = point()
blank2.x = 5.0
blank2.y = 4.0

def distance_between_points(p1, p2):
    x1 = p1.x 
    x2 = p2.x
    y1 = p1.y
    y2 = p2.y
    r = ma.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print(r)

class rectangle(object):
    """Reprensents a rectangle"""

box = rectangle()
box.width = 100.0
box.height = 200.0
box.corner = point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rectangle, dx, dy):
    rectangle.corner.x += dx
    rectangle.corner.y += dy
