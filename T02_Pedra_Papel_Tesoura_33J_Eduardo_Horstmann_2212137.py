from random import choice

numeroAleatorio = choice([i for i in range(3)])

mao = str(input('Pedra, papel ou tesoura? '))

def ppt():
    #Pedra
    if numeroAleatorio == 0:
        print('Pedra!\n')
        if mao == 'papel' or mao == 'Papel':
            return 'Ganhou'
        elif mao == 'tesoura' or mao == 'Tesoura':
            return 'Perdeu'
        elif mao == 'pedra' or mao == 'Pedra':
            return 'Empate'
    #Papel
    if numeroAleatorio == 1:
        print('Papel!\n')
        if mao == 'tesoura' or mao == 'Tesoura':
            return 'Ganhou'
        elif mao == 'pedra' or mao == 'Pedra':
            return 'Perdeu'
        elif mao == 'papel' or mao == 'Papel':
            return 'Empate'
    #Tesoura
    if numeroAleatorio == 2:
        print('Tesoura!\n')
        if mao == 'pedra' or mao == 'Pedra':
            return 'Ganhou'
        elif mao == 'papel' or mao == 'Papel':
            return 'Perdeu'
        elif mao == 'tesoura' or mao == 'Tesoura':
            return 'Empate'
        
print(ppt())
    
