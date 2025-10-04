# # dia 3 semana 1 revisão o basico em python 

# #Exercicios 1

# #part 1
# while True:
#     numero = int(input('Digite um numero: '))

#     if numero == 0:
#         print('o numero colocar foi 0 não sendo positivo nem negativo')
#         if verificardo in ['sim','s','continuar']:
#             continue
#         else:
#             print('Agradeço por participar')
#             break

#     elif numero % 2 == 0:
#         print(f'o numero colocar foi {numero} ele sendo positivo')
#         verificardo = input('deseja continuar ?')
#         if verificardo in ['sim','s','continuar']:
#             continue
#         else:
#             print('Agradeço por participar')
#             break
#     else:
#         print(f'o numero colocado foi {numero} ele sendo negativo')
#         verificardo = input('deseja continuar ?')
#         if verificardo in ['sim','s','continuar']:
#             continue
#         else:
#             print('Agradeço por participar')
#             break

# #part2

# while True:
#     idade = input('Digite sua idade: ')

#     if not idade.isnumeric() or int(idade) < 0:
#         print('Idade inválida! Tente novamente.')
#         continue


#     if int(idade) < 13:
#         print('Voce é uma criança')
#         break
#     elif int(idade) < 18:
#         print('Voce é um adolecente')
#         break
#     elif int(idade) < 60:
#         print('voce é um adulto')
#         break
#     else:
#         print('voce é um idoso')
#         break


while True:
    nota = []
    notas1 = int(input('digte a primeira nota: '))
    notas2 = int(input('digte a segunda nota: '))
    nota.append(notas1)
    nota.append(notas2)

    media = sum(nota)  / 2

    if  media >= 7:
        print('Voce esta aprovado')
    elif media >= 5:
        print('voce esta de recuperação')
    else:
        print('vc esta reprovado ')