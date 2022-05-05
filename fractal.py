import turtle
turtle.Screen().setup(800,450)

pat = turtle.Turtle()
pat.up()
pat.goto(0,-200)
pat.down()
pat.lt(90)

def galho(lado, angulo, rec, direcao, res=0):
    if rec == 0:
        return None
    if direcao == 0:
        pat.fd(lado)
        pat.lt(angulo)
        pat.fd(lado*3/4)
        pat.lt(180)
        pat.fd(lado*3/4)
        pat.lt(180-2*angulo)
        pat.fd(lado*3/4)
        pat.lt(180)
        pat.fd(lado*3/4)
        pat.lt(180+2*angulo)
        res= res +1
        for x in range(2**res):
            galho(lado*3/4, angulo, rec-1, x %2)
            pat.back(lado*3/4)
    if direcao == 1:
        pat.fd(lado)
        pat.rt(angulo)
        pat.fd(lado*3/4)
        pat.rt(180)
        pat.fd(lado*3/4)
        pat.rt(180-2*angulo)
        pat.fd(lado*3/4)
        pat.rt(180)
        pat.fd(lado*3/4)
        pat.rt(180+2*angulo)
        galho(lado*3/4, angulo, rec-1, 0)
        res= res +1
        for x in range(2**res):
            galho(lado*3/4, angulo, rec-1, x %2)
            pat.back(lado*3/4)
        

def arvore(lado, angulo, rec, res=0):
    if rec == 0:
        return None

    for x in range(2**res):
        pat.fd(lado)
        res = res +1
        pat.lt(angulo)
        arvore(lado*3/4, angulo, rec-1, res)
        
    
arvore(25, 30, 3)
    


turtle.exitonclick()
turtle.mainloop()