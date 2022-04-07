import turtle
pat = turtle.Turtle()
turtle.setup(800,450)

def propriedadesTriangulo(lado, cor_borda='black', grossura="1", lt_inicial=0):
    area = (lado**2)*(3**(1/2))/2
    perimetro = 4*lado
    pat.up()
    pat.goto(-lado/2,-lado*(3**(1/2))/4)
    pat.width(grossura)
    pat.color(cor_borda)
    pat.down()
    pat.begin_fill()
    pat.lt(lt_inicial)
    for x in range(3):
        pat.fd(lado)
        pat.lt(120)
    pat.lt(360 -lt_inicial)
    pat.up()
    pat.goto(0,0)
    return 'Área: {}\nPerímetro: {}'.format(area, perimetro)

def propriedadesQuadrado(lado, cor_borda='black', grossura="1", lt_inicial=0):
    area = lado**2
    perimetro = 4*lado
    pat.up()
    pat.goto(-lado/2,-lado/2)
    pat.width(grossura)
    pat.color(cor_borda)
    pat.down()
    pat.begin_fill()
    pat.lt(lt_inicial)
    for x in range(4):
        pat.fd(lado)
        pat.lt(90)
    pat.lt(360 -lt_inicial)
    pat.up()
    pat.goto(0,0)
    return 'Área: {}\nPerímetro: {}'.format(area, perimetro)

def propriedadesRetangulo(largura, altura, cor_borda='black', grossura="1"):
    area = largura*altura
    perimetro = (largura + altura)*2
    pat.up()
    pat.width(grossura)
    pat.color(cor_borda)
    pat.goto(-largura/2,-altura/2)
    for x in range(2):
        pat.down()
        pat.fd(largura)
        pat.lt(90)
        pat.fd(altura)
        pat.lt(90)
        pat.up()
    pat.up()
    pat.goto(0,0)
    return 'Área: {}\nPerímetro: {}'.format(area, perimetro)
        
print(propriedadesTriangulo(300))
print(propriedadesQuadrado(300))
print(propriedadesRetangulo(720, 405))


turtle.exitonclick()
turtle.mainloop()