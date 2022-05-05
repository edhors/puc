def vigenere(string, chave):
    lenStr = len(string)
    lenChv = len(chave)
    resposta = ''
    i =0
    while lenChv != lenStr:
        chave = chave + chave[i]
        lenChv = len(chave)
        i = i + 1
    for x in range(lenStr):
        letraStr = ord(string[x])
        letraChv = ord(chave[x])
        if letraStr > 90:
            letraStr = letraStr - 32
        if letraChv > 90:
            letraChv = letraChv - 32
        letra  = letraStr + letraChv - 65
        if letra > 90:
            letra = letra - 26
        resposta = resposta + chr(letra)
    return resposta

def devigenere(codigo):
    length = len(codigo)
    string = ''
    chave = ''
    for x in range(length):
        letra = ord(codigo[x])
        letraChv = 65
        while letraChv > letra:
            letraStr = letra - letraChv + 65
            letraChv = letraChv + 1
            chave = chave + chr(letraChv)
            print(chave)
        return chave
    

print(vigenere('VAMOSDESEMBARCARNANORMANDIA', 'ABACAXI'))
#print(devigenere('VBMQSAMSFMDAOKASNCNLZMBNFIX'))
    print(vigenere('attackatdawn', 'LEMON'))
#print(vigenere('cryptoisshortforcryptography', 'ABCD'))