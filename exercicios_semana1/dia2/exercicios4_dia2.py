# dia 2 semana 1 revisão o basico em python 

#Exercicios 4

alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 6.7},
    {"nome": "marcus", "nota": 10},
    {"nome": "Carla", "nota": 9.2}
    
]

media = []

for d in alunos:
    print(d['nome'])
    media.append(d['nota'])
    


mediafinal = sum(media) / len(alunos)
print(f'media de todos: {mediafinal}')



for d in alunos:
    if d['nota'] >= 7:
        print(f'{d['nome']} esta acima da media com a nota {d['nota']}')