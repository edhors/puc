def cripto(string, num =11):
    length = len(string)
    res = ''
    for x in range(length):
        letra = ord(string[x])+num
        if num >= 0:
            while letra > 122:
                letra = letra - 91
        else:
            while letra < 32:
                letra = 91 + letra
        res = res + chr(letra)
    return string+ "\n"+ res

print(cripto('atacarBerlimAs23horas hoje+1dia', 11))
