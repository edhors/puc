import turtle 
turtle.Screen().setup(1600,900)
turtle.Screen().bgcolor('black')
pat = turtle.Turtle()
turtle.colormode(255)
pat.pencolor(255,0,0)
pat.speed(0)

def estrela(x0, y0, lado, repeticao, fracao, head=0, pontas=5):
    if head == 0:
        pat.setheading(108)
    if pontas > 0:
        pat.up()
        pat.goto(x0, y0)
        pat.down()
        pat.fd(lado)
        pat.lt(144)
        x = pat.xcor()
        y = pat.ycor()
        if repeticao > 1:  
            pat.bk(lado*fracao)
            x = pat.xcor()
            y = pat.ycor()
            estrela(x, y, lado*fracao, repeticao-1, fracao, 1)
        estrela(x, y, lado, repeticao, fracao, 1, pontas-1)

turtle.Screen().tracer(1) 
estrela(50, -200, 400, 3, 1/4)
pat.clear()
turtle.Screen().tracer(3) 
estrela(50, -200, 400, 4, 1/3)
pat.clear()
turtle.Screen().tracer(5) 
estrela(50, -200, 400, 5, 1/2)

turtle.Screen().update() 
turtle.exitonclick()
turtle.mainloop()