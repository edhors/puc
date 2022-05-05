import turtle 
turtle.Screen().setup(800,450)
pat = turtle.Turtle()

pat.lt(90)

def arvore(x0, y0, lado, angulo, rep, r=0):
    if rep > 0:
        pat.up()
        pat.goto(x0, y0)
        pat.down()
        pat.fd(lado)
        if r == 0:
            pat.lt(angulo)
        if r == 1:
            pat.rt(angulo)
        x = pat.xcor()
        y = pat.ycor()
        if r ==0:
            for a in range(2):
                arvore(x, y, lado*3/4, angulo, rep-1, r)
                pat.rt(rep*angulo)
                r = 1
        if r ==1:
            for a in range(2):
                arvore(x, y, lado*3/4, angulo, rep-1, r)
                pat.lt(rep*angulo)
                r = 0
        
    

arvore(0, -200, 100, 15, 4)

turtle.exitonclick()
turtle.mainloop()