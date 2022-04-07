import numpy as np

def prod(cod):
    x1 = int(cod/1000)
    x2 = int((cod - x1*1000)/100)
    x3 = int((cod - x1*1000 - x2*100)/10)
    x4 = int(cod - x1*1000 - x2*100 - x3*10)
    return (x1*10+x2)*15+x3*10 + x4 - ((x1*10+x2)*15+x3*10 + x4)*(x3*10+x4)/100
#print(prod(2314))
   
ages = {}
def idade(i1,i2,i3,i4,i5,i6 ):
    idades = [i1,i2,i3,i4,i5,i6]
    ages[0] = i1
    ages[1] = i2
    ages[2] = i3
    ages[3] = i4
    ages[4] = i5
    ages[5] = i6
    n1 = 0
    n2 = 0
    for x in range(6):
        if(ages[x] < 18):
            n1 = n1 +1
        else:
            n1 = n1
    for x in range(6):
        if(ages[x] > 20):
            n2 = n2 +1
        else:
            n2 = n2
    print('Há {} pessoas com menos de 18 anos'.format(n1))
    print('A média das idades é {}'.format((i1+i2+i3+i4+i5+i6)/6))
    print('{} é a a maior idade'.format(np.amax(idades)))
    print('{}% das pessoas tem mais de 20'.format(n2*100/6))
    return ''
#print(idade(17, 17, 17, 34, 34, 34))

#6) Uma empresa realiza excursões desde que as seguintes regras sejam obedecidas:
#• grupo de no mínimo 5 pessoas
#• pelo menos a metade dos participantes deve ser maior de idade
#• não pode haver integrantes com menos de 11 anos
#• o integrante mais velho será escolhido o líder da excursão.
#Faça um programa que leia o nome e a idade das pessoas de uma excursão e diga se este grupo satisfaz as regras e pode
#participar da excursão (informando, também, o nome do seu líder) ou se este grupo não satisfaz as regras e, por isso, não
#pode participar desta excursão.
def get_key(val, cache):
    for key, value in cache.items():
         if val == value:
             return key
pessoa= {}  
ida= {}
def grupo(n):
    if n < 5:
        return 'O grupo deve ter no mínimo 5 pessoas'
    n18 = 0
    for x in range(n):
        nome = str(input('Nome: '))
        pessoa[x] = nome
        numero = int(input('Idade: '))
        ida[x]= numero
        if (ida[x] < 11):
            return 'Proibido menores de 11 anos'
        if (ida[x] >= 18):
            n18 = n18 + 1
    idas = [ida[x]for x in range(n)]
    maiorIda = np.amax(idas)
    maior = get_key(maiorIda, ida)
    if(n18 < n/2):
        return 'Ao menos metade dos participantes devem ser maiores de idade'
    return 'O grupo está hapto a participar da excursão e {} será o líder'.format(pessoa[maior])

#7) Faça um programa que obtenha do teclado N valores (inteiros e positivos) e teste quais valores estão dentro e quais 
#estão fora do intervalo [1...15], escrevendo o valor e a mensagem correspondente. O valor de N também deve ser lido.
#No final, seu programa deve exibir:
#• a quantidade, soma e média aritmética dos valores dentro do intervalo;
#• Quantidade de valores e o maior valor fora do intervalo.
#Exemplo:
#Entrada Saída
#Quantos números? 5
#Número? 3 3 está dentro do intervalo
#Número? 18 18 está fora do intervalo
#Número? 7 7 está dentro do intervalo
#Número? 50 50 está fora do intervalo
#Número? 22 22 está fora do intervalo
#2 valores dentro do intervalo, soma = 10 e média = 5
#3 valores fora do intervalo, maior = 50
dic = {}
lis = [1,2,4,20]
def intervalo(lista, x0 = 1, xn=15):
    l = list(range(x0, xn+1))
    inter = [(x)for x in l]
    for x in range(len(lista)):
        if lista[x] in inter:
            
            
        else:
            return '{} não está no intervalo'.format(lista)

print(lis[0])
