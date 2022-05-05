import turtle 
turtle.Screen().setup(800,450)
pat1 = turtle.Turtle()
pat2 = turtle.Turtle()
pat2.pencolor('red')
pat1.speed(1)

pat1.fd(100)
pat2.fd(-100)
pat2.lt(90)
pat2.fd(100)

turtle.exitonclick()
turtle.mainloop()