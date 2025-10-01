# dia 1 semana 1 revisão o basico em python 

#Exercicios 5 semana 1

import datetime

data = datetime.datetime.now()
string = str(data)
print(f"dia {string[8:10]}, mes {string[5:7]}, ano {string[0:4]}")