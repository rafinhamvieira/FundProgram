'''
month = int(input("what number of the month? "))

if month == 1:
    print('the month  is january!')
elif month == 2:
    print('the month is february!')
elif month == 3:
    print('the month is march!')
elif month == 4:
    print('the month is april!')
elif month == 5:
    print('the month is may!')
elif month == 6:
    print('the month is june')
elif month == 7:
    print('the month is july')
elif month == 8:
    print('the month is august!')
elif month == 9:
    print('the month is september!')
elif month == 10:
    print('the month is october!')
elif month == 11:
    print('the month is november!')
elif month == 12:
    print('the month is december!')
else:
    print('that not a month!')
'''

'''
dado_do_primeiro_lado = int(input("tamanho do primeiro lado:  "))
dado_do_segundo_lado = int(input("tamanho do segundo lado:  "))
dado_do_terceiro_lado = int(input("tamanho do terceiro lado:  "))


if dado_do_primeiro_lado == dado_do_segundo_lado and dado_do_segundo_lado == dado_do_terceiro_lado:
    print('esse triangulo é equilatero')
    if dado_do_primeiro_lado != dado_do_segundo_lado and dado_do_segundo_lado != dado_do_terceiro_lado:
            print('esse triangulo é retângulo')
    else: 
            print("esse triangulo não é retangulo")
elif dado_do_primeiro_lado != dado_do_segundo_lado and dado_do_segundo_lado != dado_do_terceiro_lado:
    print('esse triangulo é escaleno')
    if dado_do_primeiro_lado != dado_do_segundo_lado and dado_do_segundo_lado != dado_do_terceiro_lado:
        print('esse triangulo é retângulo')
    else:
        print('esse triangulo não é retangulo')
elif dado_do_primeiro_lado == dado_do_segundo_lado and dado_do_segundo_lado != dado_do_terceiro_lado:
    print('esse triangulo é isosceles')
    if dado_do_primeiro_lado != dado_do_segundo_lado and dado_do_segundo_lado != dado_do_terceiro_lado:
        print('esse triangulo é retângulo')
    else:
        print('esse triangulo não é retangulo')
elif dado_do_primeiro_lado != dado_do_segundo_lado and dado_do_segundo_lado == dado_do_terceiro_lado:
    print('esse triangulo é isosceles')
    if dado_do_primeiro_lado != dado_do_segundo_lado and dado_do_segundo_lado != dado_do_terceiro_lado:
        print('esse triangulo é retângulo')
    else:
        print('esse triangulo não é retangulo')
'''
'''
jogada1 = 'pedra'
jogada2 = 'tesoura'
jogada3 = 'papel'

print('pedra, papel, tesoura...')

jogador1 = input('qual a sua escolha jogador 1? ')
jogador2 = input('qual a sua escolha jogador 2?(nao vale olhar a jogada de cima!!!) ')

if jogador1 == jogada1 and jogador2 == jogada1:
    print('empate')
elif jogador1 == jogada1 and jogador2 == jogada2:
    print('jogador 1 ganhou a rodada')
elif jogador1 == jogada1 and jogador2 == jogada3:
    print('jogador 2 ganhou a rodada')
elif jogador1 == jogada2 and jogador2 == jogada1:
    print('jogador 2 ganhou a rodada')
elif jogador1 == jogada2 and jogador2 == jogada2:
    print('empate')
elif jogador1 == jogada2 and jogador2 == jogada3:
    print('jogador 1 ganhou a rodada')
elif jogador1 == jogada3 and jogador2 == jogada1:
    print('jogador 2 ganhou a rodada')
elif jogador1 == jogada3 and jogador2 == jogada2:
    print('jogador 2 ganhou a rodada')
elif jogador1 == jogada3 and jogador2 == jogada3:
    print('empate')
'''