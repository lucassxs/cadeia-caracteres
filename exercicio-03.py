########## Exercicio 3 #############

a = str(input("Digite uma String para A: "))

b = str(input("Digite uma String para B: "))

if a[len(a)-1] == b[len(b)-1]:
    print("Os sufixos (último caractere) entre A e B são iguais")
else:
    print("Os sufixos (último caractere) entre A e B não são iguais")
