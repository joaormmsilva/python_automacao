# dia 1 semana 1 revisão o basico em python 

#Exercicios 8 semana 1

def conta_vogais(s):
    cont = 0
    for vogal in s:
        if vogal in 'aeiou':
            cont += 1
    return f'A quantia de vogais é {cont}'


frase = input('digite uma frase: ')

print(conta_vogais(frase))
