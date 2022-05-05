import turtle

screen = turtle.Screen()
pat = turtle.Turtle()
screen.setup(800, 500)

#Polígonos equiláteros regulares
def eq(x0, y0, nlado, lado, cor='black', cor_borda='black', grossura_borda=1, lt_inicial= 0):
    pat.color(cor_borda)
    pat.fillcolor(cor)
    pat.width(grossura_borda)
    pat.up()
#Aqui defino o ponto inicial do polígono sem usar goto; pat.goto(x0, y0) seria bem melhor
    if (x0 >=0 and y0 >=0 ):
        pat.fd(x0)
        pat.lt(90)
        pat.fd(y0)
        pat.lt(270)
    elif(x0 <=0 and y0 >=0 ):
        pat.lt(180)
        pat.fd((-1)*x0)
        pat.lt(270)
        pat.fd(y0)
        pat.lt(270)
    elif (x0 >=0 and y0 <=0):
        pat.fd(x0)
        pat.lt(270)
        pat.fd((-1)*y0)
        pat.lt(90)
    elif (x0 <=0 and y0 <=0) :
        pat.lt(180)
        pat.fd((-1)*x0)
        pat.lt(90)
        pat.fd((-1)*y0)
        pat.lt(90)
    pat.lt(lt_inicial)
    pat.down()
    pat.begin_fill()
    for x in range(nlado):
        pat.fd(lado)
        pat.lt(180-180*(nlado-2)/nlado)
    pat.end_fill()
    pat.up()
    pat.goto(0,0)
    lt_final = 360 - lt_inicial
    pat.lt(lt_final)
    
    
#Retângulo
def rect(x0, y0, largura, altura, cor='black', cor_borda='black', grossura_borda=1):
    pat.color(cor_borda)
    pat.fillcolor(cor)
    pat.width(grossura_borda)
    pat.up()

#Aqui defino o ponto inicial do retângulo sem usar goto; pat.goto(x0, y0) seria bem melhor
    if (x0 >=0 and y0 >=0 ):
        pat.fd(x0)
        pat.lt(90)
        pat.fd(y0)
        pat.lt(270)
    elif(x0 <=0 and y0 >=0 ):
        pat.lt(180)
        pat.fd((-1)*x0)
        pat.lt(270)
        pat.fd(y0)
        pat.lt(270)
    elif (x0 >=0 and y0 <=0):
        pat.fd(x0)
        pat.lt(270)
        pat.fd((-1)*y0)
        pat.lt(90)
    elif (x0 <=0 and y0 <=0) :
        pat.lt(180)
        pat.fd((-1)*x0)
        pat.lt(90)
        pat.fd((-1)*y0)
        pat.lt(90)    
    pat.down()
    pat.begin_fill()
    for x in range(2):
        pat.fd(largura)
        pat.lt(90)
        pat.fd(altura)
        pat.lt(90)
    pat.end_fill()
    pat.up()
    pat.goto(0,0)
    

rect(-400, -100,800,550 ,'DeepSkyBlue', 'DeepSkyBlue' )#ceu
rect(-400, -225,800,125 ,'green', 'green' )#chao
eq(-150, -100, 4, 100, 'DarkGoldenrod4', 'DarkGoldenrod4')#casa
eq(-170, 0, 3, 140, 'brown4', 'brown4')#telhado
rect(-90, -100, 30,60 ,'brown', 'brown' )#porta
eq(-130, -60, 4, 20, 'blue', 'blue')#janela
rect(-121, -60,2,20 ,'black', 'black' )#janela
rect(-130, -50,20,2 ,'black', 'black' )#janela
rect(200, -100, 40,100 ,'DarkGoldenrod4', 'DarkGoldenrod4' )#arvore
eq(220, 0, 100, 5, 'green', 'green')#folhas
eq(200, -10, 100, 5, 'green', 'green')#folhas
eq(240, -10, 100, 5, 'green', 'green')#folhas
eq(-350, 100, 3, 100, 'orange', 'orange')#raios de sol
eq(-250, 160, 3, 100, 'orange', 'orange',1,180)#raios de sol
eq(-300, 100, 100, 2, 'yellow', 'yellow')#sol
eq(0, 100, 120, 2, 'white', 'DarkGrey')#nuvem
eq(80, 100, 120, 2, 'white', 'DarkGrey')#nuvem
eq(40, 100, 120, 2, 'white', 'DarkGrey')#nuvem

#print(eq(0, 0, 4, 400, 'darkgreen', 'darkgreen', 1))

#print(eq(-400, -400, 4, 400, 'blue', 'blue', 1))
#print(eq(0, -400, 4, 400, 'blue', 'blue', 1))

#print(eq(-100,-50 , 4, 100, 'DarkGoldenrod4', 'DarkGoldenrod4', 1))
#print(eq(-120,50 , 3, 140, 'burlywood4', 'burlywood4', 1))


turtle.exitonclick()
turtle.mainloop()