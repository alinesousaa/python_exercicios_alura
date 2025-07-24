import os

def impar_par():
    numero_usuario = int(input("Digite um número: "))
    if numero_usuario % 2 == 0:
        os.system('cls')
        print("O número é par.")
    else:
        os.system('cls')
        print("O número é ímpar.")

impar_par()