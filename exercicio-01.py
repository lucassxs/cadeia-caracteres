########## Exercicio 01 #############

def contagem(palavra):
    vogais = "aeiou"
    total = 0

    for letra in palavra:
        if letra in vogais:
            total += 1

    return total


palavra = str(input("Digite uma palavra"))
print ("Total de letras: %d - %d " % (len(palavra), (vogais)))