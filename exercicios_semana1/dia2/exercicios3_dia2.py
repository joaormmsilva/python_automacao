# dia 2 semana 1 revisão o basico em python 

#Exercicios 3 

dicionario = {'nome': 'joao', 'idade': 22, 'curso': 'adm'}

dicionario['cidade'] = 'taubate'

dicionario['curso'] = 'ti'

del dicionario['idade']

for c,v in dicionario.items():
    print(f'{c}: {v}')