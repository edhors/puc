import turtle 
turtle.Screen().setup(800,450)
pat = turtle.Turtle()
turtle.speed("fastest")
pat.lt(90)

def arvore(x0, y0, lado, angulo, repeticao, direcao=0):
    if repeticao > 0:
        pat.up()
        pat.goto(x0, y0)
        pat.down()
        pat.fd(lado)
        if direcao == 0:
            pat.lt(angulo)
        else:
            pat.rt(angulo)
        x = pat.xcor()
        y = pat.ycor()
        if direcao == 0:
            arvore(x, y, lado*3/4, angulo, repeticao-1, 0)
            pat.rt(3*angulo)
            arvore(x, y, lado*3/4, angulo, repeticao-1, 1)
            pat.lt(3*angulo)
        else:
            arvore(x, y, lado*3/4, angulo, repeticao-1, 1)
            pat.lt(3*angulo)
            arvore(x, y, lado*3/4, angulo, repeticao-1, 0)
            pat.rt(3*angulo)            
        
arvore(0, -200, 100, 45, 4)

turtle.exitonclick()
turtle.mainloop()