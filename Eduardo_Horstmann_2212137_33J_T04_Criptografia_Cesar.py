def cesar(string, num =11):
    length = len(string)
    resposta = ''
    for x in range(length):
        letra = ord(string[x])+num
        if num > 0:
            while letra > 122:
                letra = letra - 91
        else:
            while letra < 32:
                letra = 91 + letra
        resposta = resposta + chr(letra)
    return string + "\n" + resposta

print(cesar('atacarBerlimAs23horas hoje+1dia')+"\n")
print(cesar('l$lnl"Mp"wtxL#=>sz"l#+szup6<otl', -11))#o número negativo decriptografa a mensagem
