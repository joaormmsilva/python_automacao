# dia 1 semana 1 revisão o basico em python 

#Exercicios 3 semana 1
print('-'*10)
print('Gerador de medias')
print('-'*10)

nota = []

for i in range(3):
    notas = float(input(f'digite a nota da {i+1} prova: '))
    nota.append(notas)

total = sum(nota)
media = total / len(nota)

print(f"\nA sua media final é {media:.2f}")
if media < 6:
    print('Voce Esta de recuperação =(')
else:
    print('parabens vc esta aprovado!!')