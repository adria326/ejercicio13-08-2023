def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

palabra = input("ingrese una palabra: ")
print("numero de vocales:", contar_vocales(palabra))