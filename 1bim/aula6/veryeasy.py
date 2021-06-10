'''
Leia um número inteiro que representa um código de DDD para discagem
interurbana. Em seguida, informe à qual cidade o
DDD pertence, considerando a tabela abaixo. Se a
entrada for qualquer outro DDD que não esteja
presente na tabela acima, o programa deverá
informar: DDD não cadastrado
'''
import os
import time

while True:
    os.system('color 2') 
    os.system('cls')
    print()
    print('**************** CONSULTA DE DDD INTERESTADUAL ****************')
    print()
    ddd = int(input('Informe o DDD do estado desejado: '))
    print()
    print('**************** VERIFICANDO NO SISTEMA... **************** ')
    print()
    if ddd == 61:
        print('Esse DDD é de Brasília! ')
        time.sleep(4)
    elif ddd == 71:
        print('Esse DDD é de Salvador! ')
    elif ddd == 11 or ddd == 12 or ddd == 13 or ddd == 14 or ddd == 15 or ddd == 16 or ddd == 17 or ddd == 18 or ddd == 19:
        print('Esse DDD é de São Paulo! ')
        time.sleep(4)
    elif ddd == 21 or ddd ==22 or ddd == 24:
        print('Esse DDD é do Rio de Janeiro! ')
        time.sleep(4)
    elif ddd == 32:
        print('Esse DDD é de Juíz de Fora! ')
        time.sleep(4)
    elif ddd == 19:
        print('Esse DDD é de Campinas! ')
        time.sleep(4)
    elif ddd == 27:
        print('Esse DDD é de Vitória! ')
        time.sleep(4)
    elif ddd == 31:
        print('Esse DDD é de Belo Horizonte! ')
        time.sleep(4)
    elif ddd == 54:
        print('Esse DDD é de Passo Fundo! ')
        time.sleep(4)
    elif ddd == 55:
        print('Esse DDD é de Porto Alegre! ')
        time.sleep(4)
    elif ddd == 82:
        print('Esse DDD é de Alagoas! ')
        time.sleep(4)
    elif ddd == 83:
        print('Esse DDD é de Paraíba! ')
        time.sleep(4)
    elif ddd == 84:
        print('Esse DDD é do Rio Grande do Norte! ')
        time.sleep(4)
    elif ddd == 79:
        print('Esse DDD é de Sergipe! ')
        time.sleep(4)
    elif ddd == 68:
        print('Esse DDD é do Acre! ')
        time.sleep(4)
    elif ddd == 96:
        print('Esse DDD é de Amapá! ')
        time.sleep(4)
    elif ddd == 69:
        print('Esse DDD é de Rondônia! ')
        time.sleep(4)
    elif ddd == 95:
        print('Esse DDD é de Roraima! ')
        time.sleep(4)
    elif ddd == 63:
        print('Esse DDD é de Tocantins! ')
        time.sleep(4)
    elif ddd == 47 or ddd == 48 or ddd == 49:
        print('Esse DDD é de Santa Catarina! ')
        time.sleep(4)
    elif ddd == 41 or ddd == 42 or ddd == 43 or ddd == 44 or ddd == 45 or ddd == 46:
        print('Esse DDD é do Paraná! ')
        time.sleep(4)
    else:
        print('DDD não encontrado na lista! ')
        time.sleep(4)