import rhinoscriptsyntax as rs
import math as ma
import random as rd

def delete_all():
    all_objects = rs.ObjectsByType(0)
    rs.DeleteObjects(all_objects)

def delete_something(n):
    something = rs.ObjectsByType(n)
    rs.DeleteObjects(something)

a = 0.1
b = 0.01
g = 1.0
t = 0.0
dt = 0.01
L = 0.5

class Firefly:
    
    def __init__(self, nod, x, group, nop):
        self.nod = nod
        self.x = x
        self.group = group
        self.nop = nop
    
    def evaluate(self):
        func = self.x[0]*self.x[1]*ma.sin(2*ma.pi*self.x[0])*ma.cos(2*ma.pi*self.x[1])
        self.ri = func
    
    def move(self):
        for target in self.group:
            if self.ri < target.ri:
                r2 =0.0
                for i in range(0,self.nod):
                    r2 = r2 + (self.x[i]-target.x[i])**2
                for i in range(0,self.nod):
                    ex = (rd.random() - 0.5)*L
                    self.x[i] = self.x[i] + b*ma.exp(-g*r2)*(target.x[i]-self.x[i])+ a*ex*ma.exp(-t)
    def display(self):
        rs.AddCircle([self.x[0]*50, self.x[1]*50, 0], 0.5)

swarm = []
nod = 2

def look_for_firefly(nop):
    for i in range(0, nop):
        x =[]
        for k in range(0, nod):
            x.append(rd.random())
        swarm.append(Firefly(nod, x, swarm, nop))
        
        t = 0.0
        dt = 0.01
        for step in range(0, 500):
            t = t + dt
            for one in swarm:
                one.evaluate()
            for one in swarm:
                one.move()
        
        for one in swarm:
            one.display()
            print one.x[0],one.x[1]

look_for_firefly(50)

