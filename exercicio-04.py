########## Exercicio 04 #############

def palindromo(pala):
    if pala == pala[::-1]:
        return True
    return False


palavra = input('Digite uma palavra: ').lower().strip().replace(' ', '')

print(palindromo(palavra))