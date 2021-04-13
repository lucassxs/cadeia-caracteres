########## Exercicio 02 #############
def fun (prefixo):
    pre = 1
    
    for i in range(len(prefixo)):
        if prefixo [i] == ("ab", "ambi", "ante", "bem", "bi", "contra", "in", "pos", "semi", "tri" ):
            pre += 1
            
    return pre
a = str(input("Digite uma palavra"))
print(prefixo)