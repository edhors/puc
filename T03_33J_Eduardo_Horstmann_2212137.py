import turtle 
turtle.Screen().setup(800,450)
pat = turtle.Turtle()
pat.lt(90)

def arvore(x0, y0, lado, angulo, repeticao, fator, direcao=0):
    if repeticao > 0:
        pat.up()
        pat.goto(x0, y0)
        pat.down()
        pat.fd(lado)
        if direcao == 0:
            pat.lt(angulo)
            x = pat.xcor()
            y = pat.ycor()
            arvore(x, y, lado*fator, angulo, repeticao-1, fator,0)
            pat.rt(3*angulo)
            arvore(x, y, lado*fator, angulo, repeticao-1, fator,1)
            pat.lt(3*angulo)
        else:
            pat.rt(angulo)
            x = pat.xcor()
            y = pat.ycor()
            arvore(x, y, lado*fator, angulo, repeticao-1, fator, 1)
            pat.lt(3*angulo)
            arvore(x, y, lado*fator, angulo, repeticao-1, fator, 0)
            pat.rt(3*angulo)            
        
arvore(0, -200, 100, 30, 7, 0.8)

turtle.exitonclick()
turtle.mainloop()