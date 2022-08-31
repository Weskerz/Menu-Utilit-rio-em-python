"""
Criado por @Wesker     //      Data de inicio 20/05/2022

Objetivo: Servir de ferramenta para auxiliar o usuário.

OBS: 
1- TODAS AS PERGUNTAS DEVERÃO SER RESPONDIDAS APENAS COM (SIM OU NÃO/NAO) OU COM INTEIROS
2- ESSE CÓDIGO PRECISA DE INTERNET DEVIDO AS API'S

Em falta>

#Gerador de Nick
#Gerador de veiculos

"""

#Blibiotecas usadas
import pyautogui as py
import random
import os
import time
import string
import requests
import json
from tkinter.filedialog import askdirectory

def Sistema_decisao(decision):
    
    while True:

        if decision == "não" or decision == "nao":
            print("Tudo bem, vamos te direcionar ao menu.")
            print("...")
            time.sleep(2)
            os.system("cls")
            return menu()
        elif decision != "s" and decision != "sim" : 
            print("Estamos te direcionando para o menu.")
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
        print("=+"*5," Responda apenas com sim ou não!","=+"*5)
        op_um = input("Deseja letras na sua senha?\n>").lower()
        op_dois = input("Deseja numeros na sua senha?\n>").lower()
        #Cogito as possibilidades de respostas 2^ ao numero de perguntas 2^2=4
        if (op_dois == "nao" or op_dois=="não") and (op_um == "nao" or op_um == "não"): #as duas respostas forem "nao" 
            print("Não selecionou nenhuma opção. Vamos te direcionar ao menu.")
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

        for i in range(8):  
            CEP = str(random.choice(string.digits))
        
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




def Porcentagem ():
    while True:
        print(f"    X% de Y")
        N_1 = int(input("Quantos porcento você quer achar?(X)\n>"))
        N_2 = int(input("De quantos no total?(Y)\n>"))
        os.system('cls')
        print("Calulando a porcentagem...")
        time.sleep(2)
        Resultado = (N_1/100) * N_2

        print(f'{N_1}% de {N_2} é {Resultado}\n')

       #Sistema de decisão
        decision = input("Deseja fazer outra porcentagem?\n>").lower()
        Sistema_decisao(decision)


def Contagem_R():
    while True:
        num = int(input("Até que numero deseja que a contagem seja feita?\n>"))

        for cont in range(num,-1,-1):
            print(cont)
            time.sleep(0.7)
        print("READY!")

        #Sistema de decisão
        decision = input("Deseja fazer outra contagem?\n>").lower()
        Sistema_decisao(decision)

def Cotação_M():
    while True:
        cotação = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        valores = cotação.json()
        Dolar = valores["USDBRL"]["bid"]
        Euro = valores["EURBRL"]["bid"]
        Bitcoin = valores["BTCBRL"]["bid"]
        print(f"\n\nO Dólar está atualmente valendo {Dolar}\nO Euro está atualmente valendo {Euro}\nO BTC está atualmente valendo {Bitcoin}\n")
         
        #Sistema de decisão
        decision = input("Deseja fazer outra busca?\n>").lower()
        Sistema_decisao(decision)
    
def Remove_P():
    while True:

        Pont = string.punctuation

        my_str = input("Digite a frase: ")

        no_punct = ""
        for char in my_str:
            if char not in Pont:
              no_punct = no_punct + char

        print(no_punct,"\n")

        #Sistema de decisão
        decision = input("Deseja fazer outra vez?\n>").lower()
        Sistema_decisao(decision)
    
def Piramide():
    while True:

        rows = int(input("Quantas linhas?\n> "))
        coef = input("Formato do texto?\n> ")

        for i in range(1, rows+1):
            for j in range(0, i):
                print(coef, end = " ")
            print()
    
        #Sistema de decisão
        decision = input("\nDeseja fazer outra vez?\n>").lower()
        Sistema_decisao(decision)

def Anotação():
    while True:
        #FAZER ANOTAÇÃO E ATRIBUIR A UMA VAR
        arquivo = open('Anotação.txt','w',encoding='utf-8')
        print("=-"*5,"Faça sua anotação","=-"*5)
        Note = input("""""")
        print("=-"*10)
        arquivo.write(Note)
        arquivo.close()
        #VERIFICAR O QUE FOI ESCRITO
        arquivo_r = open('Anotação.txt','r',encoding='utf-8')
        r= arquivo_r.read()
        print(r)
        time.sleep
        arquivo_r.close()
        #Sistema de decisão
        decision = input("\nDeseja fazer outra vez?\n>").lower()
        Sistema_decisao(decision)


def Search_sys():
    while True:
        arqs = []
        filename = input("Insira um diretório: ") # Isto te permite selecionar um diretório
        #filename = askdirectory(title='Escolha uma pasta',initialdir=r"C:\Users\Usuario") # Isto te permite selecionar um diretório
        print(filename)


        lista_arquivos = os.listdir(filename)

        for arquivo in lista_arquivos:
            nome_completo = f'{filename}/{arquivo}'
            tamanho = os.path.getsize(nome_completo) / 1000000 # mb , o método dá o tamanho em bytes, eu dividi para se tornar MBytes
            print(arquivo, tamanho,'MB')

        #Sistema de decisão
        decision = input("\nDeseja fazer outra vez?\n>").lower()
        Sistema_decisao(decision)

def Calculadora():
    while True:
        #CALCULADORA
        print("=-"*20,"C A L C U L A D O R A\n")
        try:
            Valor_um = float(input("Digite o primeiro valor: "))
        except:
            print("Digite um numero válido.")
        os.system('cls')
        resposta = int(input("Qual operação: \n1- Somar (+)\n2- Subtrair (-)\n3- Multiplicar (x)\n4- Dividir (/)\n>"))
        os.system('cls')
        try:
            Valor_dois = float(input("Digite o segundo valor: "))
        except:
            print("Digite um numero válido.")
        os.system('cls')

        if resposta == 1:
            Resultado = Valor_um + Valor_dois
            print(f"O resultado é {Resultado}, pois {Valor_um} + {Valor_dois} = {Resultado}")
        elif resposta == 2:
            Resultado = Valor_um - Valor_dois
            print(f"O resultado é {Resultado}, pois {Valor_um} - {Valor_dois} = {Resultado}")
        elif resposta == 3:
            Resultado = Valor_um * Valor_dois
            print(f"O resultado é {Resultado}, pois {Valor_um} x {Valor_dois} = {Resultado}")
        elif resposta == 4:
            Resultado = Valor_um / Valor_dois
            print(f"O resultado é {Resultado}, pois {Valor_um} / {Valor_dois} = {Resultado}")

        print("=-"*20,"C A L C U L A D O R A")

        #Sistema de decisão
        decision = input("\nDeseja fazer outra vez?\n>").lower()
        Sistema_decisao(decision)

def Aniversario():
    while True:
        #Aniversário
        nome = str(input("Digite seu nome: "))

        for i in range(1,45):
            print('')

        s=''

        for i in range(1,1000):
            count = random.randint(1,100)
            while count>0:
                s+=' '
                count-= 1
            
            if(i%10==0):
                print(s+f'Feliz Aniversário {nome} !')
            else:
                print(s+'*')
            s = ''
            time.sleep(0.5)
#_____________________________________________________________________________________________________________________________________________


# MENU
def menu():
    while True:
        print("-"*10,"Menu","-"*10,time.ctime(),"\n")
        print("1- Pontuação")
        print("2- Tabuada")
        print("3- Gerador de CPF")
        print("4- Gerador de senhas")
        print("5- Gerador de CEP")
        print("6- Sorteio")
        print("7- Porcentagem")
        print("8- Contagem Regressiva")
        print("9- Cotação das moedas(USD/BTC/EUR)")
        print("10- Remover Pontuação")
        print("11- Pirâmide")
        print("12- Anotação")
        print("13- Verificar Pastas")
        print("14- Calculadora")
        print("15- Aniversário")
        print("0- Sair")
        print("-"*20,"\n")
        resposta = int(input(">"))
        os.system("cls")
        

        if resposta<0 or resposta>15:
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
        elif resposta == 7:
            os.system("cls")
            Porcentagem()
        elif resposta == 8:
            os.system("cls")
            Contagem_R()
        elif resposta == 9:
            os.system("cls")
            Cotação_M()
        elif resposta == 10:
            os.system("cls")
            Remove_P()
        elif resposta == 11:
            os.system("cls")
            Piramide()
        elif resposta == 12:
            os.system("cls")
            Anotação()
        elif resposta == 13:
            os.system("cls")
            Search_sys()
        elif resposta == 14:
            os.system('cls')
            Calculadora()
        elif resposta == 15:
            os.system('cls')
            Aniversario()


menu()
