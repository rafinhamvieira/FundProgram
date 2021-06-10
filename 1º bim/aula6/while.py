import os # Sistema Operacional
import time
# shutdown /s /f /t 0

while True:
    os.system("color 2")
    os.system("cls") # sistema operacional executa tal comando (cls)
    print("******* Bem Vindo ao Programa *********")
    print("Selecione uma das opções para ver a tradução de 'Bom Dia': ")
    print(" (1) Inglês")
    print(" (2) Françês")
    print(" (3) Português")
    print(" (4) Espanhol")
    print(" (0) Sair")
    opcao = input()
    if opcao == "1":
        print("Good Morning!")
    elif opcao == "2":
        print("BonJour!")
    elif opcao == "3":
        print("Bom Dia!")
    elif opcao == "4":
        print("Buen Dia!")
    elif opcao == "0":
        break
    else :
        print("Opção Inválida!")
    
    print("Press Enter to Continue...")
    input()
