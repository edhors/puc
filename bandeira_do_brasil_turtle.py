import turtle
import numpy as np
pat = turtle.Turtle()
turtle.setup(800,450)


def eq(x0, y0, nlado, lado, cor ='black', cor_borda='black', grossura="1", lt_inicial=0):
    pat.up()
    pat.goto(x0,y0)
    pat.width(grossura)
    pat.color(cor_borda)
    pat.fillcolor(cor)
    pat.down()
    pat.begin_fill()
    pat.lt(lt_inicial)
    for x in range(nlado):
        pat.fd(lado)
        pat.lt(180-180*(nlado -2)/nlado)
    pat.end_fill()
    pat.lt(360 -lt_inicial)
    pat.up()
    pat.goto(x0,y0)


def rect(x0, y0, largura, altura, cor ='black', cor_borda='black', grossura="1"):
    pat.up()
    pat.width(grossura)
    pat.color(cor_borda)
    pat.fillcolor(cor)
    pat.goto(x0,y0)
    pat.begin_fill()
    for x in range(2):
        pat.down()
        pat.fd(largura)
        pat.lt(90)
        pat.fd(altura)
        pat.lt(90)
        pat.up()
    pat.end_fill()
    pat.up()
    pat.goto(x0,y0)

def tri(x0, y0, cat1, cat2, cor ='black', cor_borda='black', grossura="1", lt_inicial=0, angulo1=90):
    ancos = angulo1*np.pi/180
    hipo = (cat1**2 + cat2**2 -2*cat1*cat2*np.cos(ancos))**(1/2)
    angRad = np.arcsin(cat1/hipo)
    ang = angRad*180/np.pi
    pat.up()
    pat.goto(x0,y0)
    pat.width(grossura)
    pat.color(cor_borda)
    pat.fillcolor(cor)
    pat.down()
    pat.begin_fill()
    pat.lt(lt_inicial)
   
    pat.fd(cat1)
    pat.lt(180-angulo1)
    pat.fd(cat2)
    pat.lt(ang)  
   
    pat.end_fill()
    pat.lt(360-180-lt_inicial+angulo1-ang)
    pat.up()
    pat.goto(x0,y0)

rect(-400, -225,800,450 ,'green', 'green')
tri(165.5*np.sqrt(3), 0, 325, 325, 'yellow', 'yellow', 1, 150, 120 )
tri(-159*np.sqrt(3), 0, 325, 325, 'yellow', 'yellow', 1, 330, 120 )
eq(0, -88, 50, 12, 'blue', 'blue')


turtle.exitonclick()
turtle.mainloop()