"""
Criado por @Wesker     //      Data de inicio 20/05/2022

Objetivo: Servir de ferramenta para auxiliar o usuário.

OBS: TODAS AS PERGUNTAS DEVERÃO SER RESPONDIDAS APENAS COM SIM OU NÃO/NAO
     ESSE CÓDIGO PRECISA DE INTERNET DEVIDO AS API'S

Em falta>

#Cotação do Dolar/Euro/Real
#Gerador de Nick
#Gerador de veiculos
#Calcular Porcentagem de algo

"""

#Blibiotecas usadas
import random
import os
import time
import string
import requests
import json


def Sistema_decisao(decision):
    
    while True:

        if decision == "não" or decision == "nao":
            print("Tudo bem, vamos te direcionar ao menu.")
            print("...")
            time.sleep(2)
            os.system("cls")
            return menu()
        elif decision != "não" and decision != "sim":
            print("Digito incorreto, estamos te direcionando para o menu.")
            print("...")
            time.sleep(2)
            os.system("cls")
            return menu()
        else:
            os.system('cls')
            break


#Pontuação Aleatória/Satisfação/Avaliar
def Pontuação ():
    while True:
        num_um = int(input("Ate que valor a pontuação aleatória deve ser cogitada?\nDe 0 até X(sua resposta)\n>"))
        rand =random.randint(0,num_um)
        print(f"Sua pontuação é de {rand}","\n"*2)
        time.sleep(1)
        

       #Sistema de decisão
        decision = input("Deseja fazer outra pontuação?\n>").lower()
        Sistema_decisao(decision)

        
#Tabuada
def Tabuada():
     while True:

        num_tab = int(input("Qual tabuada deseja?(Apenas inteiros)\n>"))
        print("Tabuada do ", num_tab)
        for c in range(11):
          print(num_tab, "x", c, " = ", num_tab*c)
        
        
        #Sistema de decisão
        decision = input("Deseja fazer outra tabuada?\n>").lower()
        Sistema_decisao(decision)

#Gerador de CPF 
def Gerador_cpf():
    while True:
        
        print("Vamos gerar seu CPF aleatóriamente em um instante!\n")
        print("...")
        time.sleep(2)
        os.system('cls')

        #CPF 000.000.000-00
        part_um = random.randint(100,999)
        part_dois = random.randint(100,999)
        part_tres = random.randint(100,999)
        part_quatro = random.randint(10,99)

        print(f"CPF: {part_um}.{part_dois}.{part_tres}-{part_quatro}")

       

        #Sistema de decisão
        decision = input("Deseja gerar outro CPF?\n>").lower()
        Sistema_decisao(decision)

#Gerador de senhas
def Gerador_senhas():
    while True:
        #Defino letras e numeros
        letras = string.ascii_letters
        numeros = string.digits
        #Pergunto ao usuário o que ele deseja
        op_um = input("Deseja letras na sua senha?\n>").lower()
        op_dois = input("Deseja numeros na sua senha?\n>").lower()
        #Cogito as possibilidades de respostas 2^ ao numero de perguntas 2^2=4
        if (op_dois == "nao" or op_dois=="não") and (op_um == "nao" or op_um == "não"): #as duas respostas forem "nao" 
            print("Vamos te direcionar ao menu.")
            print("...")
            time.sleep(2)
            os.system('cls')
            break

        op_tres = int(input("Deseja quantos digitos(tamanho)?\n>"))

        senha ="" #defino previamente onde vou armazenar a senha
        if op_um == "sim" and op_dois == "sim": #Duas respostas sim
            for vezes in range(op_tres): #tamanho da senha definido pelo usuário
                gerador = random.choice(letras+numeros) #randomizo
                senha += gerador #faço o contador pra ir armazenando um caractere em cima do outro
            print(f"Sua senha é {senha}\n")
            print("-="*10)
        elif op_um == "sim" and (op_dois == "nao" or op_dois == "não"): #uma resposta não e outra sim
            for vezes in range(op_tres):
                gerador = random.choice(letras)
                senha += gerador
            print(f"Sua senha é {senha}\n")
            print("-="*10)
        elif op_dois == "sim" and (op_um == "nao" or op_um == "não"): #uma resposta sim e outra não
            for vezes in range(op_tres):
                gerador = random.choice(numeros)
                senha += gerador
            print(f"Sua senha é {senha}\n")
            print("-="*10)
        

        #Sistema de decisão
            decision = input("Deseja refazer?\n>").lower()
            Sistema_decisao(decision)

#Gerador de CEP
def Gerador_CEP():
    while True:
        CEP = ""
        for i in range(8):  

            DIGITO = str(random.choice(string.digits))
            CEP = str(CEP + DIGITO )

        response = requests.get(f'https://viacep.com.br/ws/{CEP}/json/')

        local = response.json()
        print(f"Verificando {CEP}")
        if  "erro" not in local: #SE O RESULTADO NÃO TEM ERRO
            print(f"""Seu Cep é {CEP}\n_______________________________
        Localidade {local['localidade']}
        Logradouro {local['logradouro']}
        Bairro {local['bairro']}
        DDD {local['ddd']}\
            """)
            break
        else:
            pass

        #Sistema de decisão
        decision = input("Deseja refazer?\n>").lower()
        Sistema_decisao(decision)

#SORTEIO DE NUMEROS
def Sorteio():
    while True:
        
        try:
            Tamanho = int(input('Até que numero o sorteio pode acontecer?\n>'))
            Quantidade = int(input('Quantos numeros você quer sortear?\n>'))
            
            #Sorteando

            for i in range(Quantidade):
                Numero_sort = random.randint(0,Tamanho)

                if Quantidade>1:
                    print(f"{i+1}º Numero sorteado: {Numero_sort}")
                    print("-="*10)
                else:
                    print(f"O numero sorteado é: {Numero_sort}")
            
            #Sistema de decisão
            decision = input("Deseja refazer?\n>").lower()
            Sistema_decisao(decision)

        except ValueError:
                print("Digite apenas numeros!")
                time.sleep(3)
                os.system('cls')
                pass
#_____________________________________________________________________________________________________________________________________________


# MENU
def menu():
    while True:
        print("-"*10,"Menu","-"*10,"\n")
        print("1- Pontuação")
        print("2- Tabuada")
        print("3- Gerador de CPF")
        print("4- Gerador de senhas")
        print("5- Gerador de CEP")
        print("6- Sorteio")
        print("0- Sair")
        print("-"*20,"\n")

        resposta = int(input(">"))
        os.system("cls")
        

        if resposta<0 or resposta>9:
            print("Digite um numero válido!")
            print("...")
            time.sleep(2)
            os.system("cls")
        elif resposta == 0:
            exit()
        elif resposta == 1:
            os.system("cls")
            Pontuação()
        elif resposta == 2:
            os.system("cls")
            Tabuada()
        elif resposta == 3:
            os.system("cls")
            Gerador_cpf()
        elif resposta == 4:
            os.system("cls")
            Gerador_senhas()
        elif resposta == 5:
            os.system("cls")
            Gerador_CEP()
        elif resposta == 6:
            os.system("cls")
            Sorteio()


menu()