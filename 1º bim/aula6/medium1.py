'''
Desenvolva um algoritmo com a capacidade de receber a KM de um veículo e a
quantidade de litros de gasolina que o mesmo consumiu. Após deve ser calculado, indicando a
média de consumo do veículo e o nível de consumo conforme tabela abaixo (Km/l). 
'''
import os
import time

while True:
   os.system('color 2') 
   os.system('cls')
   print()
   print('******* ALGORITMO QUE CALCULA A MÉDIA DE CONSUMO DE UM VEÍCULO*******')
   kilometros = int(input('Quantos Km foram feitos? '))
   print()
   litros = int(input('Quantos litros de combustível foi colocado? '))
   print()
   calculoKmLitros = kilometros / litros
   if calculoKmLitros > 12:
        print('A média do veículo foi ', calculoKmLitros, ' Km/l', ' e a classificação foi A!! ')
        time.sleep(4)
   elif calculoKmLitros > 10 and calculoKmLitros == 12:
        print('A média do veículo foi ', calculoKmLitros, ' Km/l', ' e a classificação foi B!! ')
        time.sleep(4)
   elif calculoKmLitros > 8 and calculoKmLitros == 10:
        print('A média do veículo foi ', calculoKmLitros, ' Km/l', ' e a classificação foi C!! ')
        time.sleep(4)
   elif calculoKmLitros > 4 and calculoKmLitros == 8:
        print('A média do veículo foi ', calculoKmLitros, ' Km/l', ' e a classificação foi D!! ')
        time.sleep(4)
   elif calculoKmLitros > 0 and calculoKmLitros == 4:
        print('A média do veículo foi ', calculoKmLitros, ' Km/l', ' e a classificação foi E!! ')
        time.sleep(4)


#def calculoKmLitros (kilometros, litros):