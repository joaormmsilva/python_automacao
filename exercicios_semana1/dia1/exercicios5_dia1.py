# dia 1 semana 1 revisão o basico em python 

#Exercicios 5 semana 1

import datetime

date = datetime.datetime.now()
string = str(date)
print(f"day {string[8:10]}, month {string[5:7]}, year {string[0:4]}")