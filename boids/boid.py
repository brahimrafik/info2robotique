import turtle
import random
import math

#para
N = 30
vcte=50

boid =[]
#creation des tortues
for  i in range ( N )  :
    boid.append(turtle.Turtle())
#initialisation des parametres
    boid[i].penup()
    boid[i].setposition(random.randint(-100,100),random.randint(-100,100))
    boid[i].color(random.random(),random.random(), random.random())
    boid[i].setheading(random.randint(0,359))
    boid[i].pensize(5)
    boid[i].pendown()


    


#pos moy
def pm():
    sx,sy = 0,0

    for i in range(N):
        x,y= boid[i].position()
        sx+=x
        sy+=y
    return sx/N , sy/N

#angle moyen
def ang():
    a=0
    for i in range (N):
        a+= boid[i].heading()
    return a/N


def heading2speed(angle):
    return vcte* math.cos(angle/57.17),vcte* math.sin(angle/57.17)

def speed2heading(x,y):
    return math.atan2(y,x)*57.17



while 1 :
    pmx , pmy = pm()
    angle=ang()
    
    for i in range (N):
        
        x,y= boid[i].position()
        vx= pmx-x
        vy = pmy-y
        boid[i].setheading(speed2heading(vx,vy))
        boid[i].forward(vcte)
        boid[i].pensize(5)
        boid[i].pendown()




raw_input()
