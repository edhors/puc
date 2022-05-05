"""
2ª Script – Fractal Estrela.
• Nesta tarefa, o aluno deverá desenhar um fractal estrela.
• Abaixo são apresentados alguns exemplos com fatores diferentes. O desenho
representa uma estrela de 5 pontas onde cada ponta também forma uma estrela
recursivamente.
Parâmetros padrão:
• Ângulo = 216
• Tamanho mínimo > 10
• Fator = 1/3
"""

import turtle 
turtle.Screen().setup(1200,675)
turtle.Screen().bgcolor('black')
pat = turtle.Turtle()
turtle.colormode(255)
pat.pencolor(255,0,0)
pat.speed(0)
pat.lt(108)
turtle.Screen().tracer(0) 

def estrela(x0, y0, lado, fator=0, pontas=5):
    if pontas > 0:
        pat.up()
        pat.goto(x0, y0)
        pat.down()
        pat.fd(lado)
        pat.lt(144)
        x = pat.xcor()
        y = pat.ycor()
        if fator > 1:  
            a=0
            pat.bk(lado/2.01)
            x = pat.xcor()
            y = pat.ycor()
            estrela(x, y, lado/2.01, fator-1)
            a= a+1

        estrela(x, y, lado, fator, pontas-1)
        
estrela(50, -250, 400, 5)

turtle.Screen().update() 

turtle.exitonclick()
turtle.mainloop()