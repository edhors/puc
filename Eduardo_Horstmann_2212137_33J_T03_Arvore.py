import turtle 
turtle.Screen().setup(800,450)
turtle.Screen().bgcolor('black')
pat = turtle.Turtle()
pat.speed(0)
turtle.Screen().tracer(1) 

def arvore(x0, y0, lado, angulo, repeticao, fator, direcao=0, head=0):
    if head == 0:
        pat.setheading(90)
        head = 1
    if repeticao > 0:
        turtle.colormode(255)
        pat.pencolor(0,int(255/repeticao),0)
        pat.up()
        pat.goto(x0, y0)
        pat.down()
        pat.fd(lado)
        if direcao == 0:
            pat.lt(angulo)
            x = pat.xcor()
            y = pat.ycor()
            arvore(x, y, lado*fator, angulo, repeticao-1, fator,0, 1)
            pat.rt(3*angulo)
            arvore(x, y, lado*fator, angulo, repeticao-1, fator,1, 1)
            pat.lt(3*angulo)
        else:
            pat.rt(angulo)
            x = pat.xcor()
            y = pat.ycor()
            arvore(x, y, lado*fator, angulo, repeticao-1, fator, 1, 1)
            pat.lt(3*angulo)
            arvore(x, y, lado*fator, angulo, repeticao-1, fator, 0, 1)
            pat.rt(3*angulo)            
        
arvore(0, -200, 100, 30, 7, 0.8)

turtle.exitonclick()
turtle.mainloop()