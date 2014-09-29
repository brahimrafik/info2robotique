# -*- coding: utf-8 -*-
"""
Telemetry
created by rafik Brahim
"""

from sympy.geometry import Polygon,Line,Point,intersection
from sympy import N
import turtle
import random
from math import *
import numpy as np
import matplotlib.pyplot as plt
import time

def new_box(x,y,c):
    V = turtle.Turtle()
    V.hideturtle(); V.penup()
    V.setpos(x-c/2,y-c/2); V.setheading(0) ; V.pendown()
    for i in range(4):
        V.fd(c)
        V.left(90)
    return Polygon(Point(x-c/2,y-c/2),Point(x-c/2,y+c/2),Point(x+c/2,y+c/2),Point(x+c/2,y-c/2))

def telemetry(T,boxelist):
    a = radians(T.heading())
    P1,P2 = Point(T.xcor(),T.ycor()) , Point(T.xcor()+cos(a),T.ycor()+sin(a))
    P12 = P2 - P1
    intr = [N(P12.dot(p-P1)) for r in boxelist for p in intersection(Line(P1,P2),r) ]
    intr = [d for d in intr if d >= 0]
    #print intr
    return None if intr==[] else (min(intr)+np.random.normal(0,10))
    
def turn_around(T,boxelist,n):
    mesures = [telemetry(T,boxelist)]
    for i in range(n-1):
        T.left(360.0/n)
        mesures.append(telemetry(T,boxelist))
        
    print mesures
    return mesures
    
def sortie(mesures,v):
    max=0
    compteur=0
    for i in range(len(mesures)):
        if mesures[i]<v:
            compteur=0
        else:
            compteur=compteur+1
            if(i==len(mesures)-1):
                j=i+1
                while mesures[j-len(mesures)]<v:
                    compteur=compteur+1
                    j=j+1
                if compteur>max:
                    max=compteur
                    indice=j
                
            
            else:
                if compteur>max:
                    max=compteur
                    indice=i
                
    return (indice-int(max/2))%len(mesures)
    
def escape(T,indice,n):
    T.left(indice*360.0/n)
    T.fd(200)
    
def navigate(T,boxelist,n):
    mesures = turn_around(T,boxelist,n)
    i = sortie(mesures,200)
    escape(T,i,n)

######### main ########
turtle.clearscreen()
T = turtle.Turtle()
T.penup()

boxelist = [ new_box(0,0,400) ]
boxelist = boxelist +[ new_box(100*cos(1+i*2*pi/15),100*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(12)]
boxelist = boxelist +[ new_box(170*cos(1+i*2*pi/15),170*sin(1+i*2*pi/15),random.randint(10,40)) for i in range(14)]
for i in range(5):
    navigate(T,boxelist,50)
    time.sleep(2)

raw_input()
