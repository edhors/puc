def vigenere(string, chave):
    lenStr = len(string)
    lenChv = len(chave)
    res = ''
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
        cipher  = letraStr + letraChv - 65
        if cipher  > 90:
            cipher = cipher - 26
        letra = chr(cipher)
        res = res + letra
    return res

print(vigenere('VAMOSDESEMBARCARNANORMANDIA', 'ABACAXI'))
print(vigenere('attackatdawn', 'LEMON'))
print(vigenere('cryptoisshortforcryptography', 'ABCD'))