'''
Crie um algoritmo que receba a velocidade do carro e analise se o mesmo deve ser
multado e valor que ele deve pagar. [abaixo um exemplo de saída do code]
a. Se for menor que 80 não haverá multa.
b. Se estiver entre 80 e 95, a multa é infração leve e o valor a ser pago é de R$ 67,00
c. Se estiver acima de 95, a multa é infração grave e o valor a ser pago é de R$ 187,00
'''
import os
import time

while True:
    os.system('color 2') 
    os.system('cls')
    print()
    print('********** SISTEMA VERIFICADOR DE VELOCIDADE DA PRF ***********')
    veloc = int(input('Qual a velocidade do carro? em Km/H? '))
    print('******** Verificando no sistema... ********')
    time.sleep(2)
    if veloc > 95:
        print('A multa é infração grave e o valor a ser pago é de R$ 187,00')
        time.sleep(4)
    elif veloc <= 95 and veloc >= 80:
        print('a multa é infração leve e o valor a ser pago é de R$ 67,00')
        time.sleep(4)
    elif veloc < 80:
        print('Velocidade OK, Sem multas! ')
        time.sleep(4)