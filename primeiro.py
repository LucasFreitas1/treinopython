import os
import random

print ("Criando um programa a base do Python")


def limpaTela():
    os.system('cls')
def calcErro():
    limpaTela()
    print("Operação não suportada. Somente disponivel: \n Multiplicação, Divisão, Soma e Subtração \nTente novamente\n")
    
def calculadora():
    print("**** Calculadora ****")
    print("Digite o primeiro numero: ")
    n1 = int(input())
    print("Digite o segundo numero: ")
    n2 = int(input())
    print("Selecione a operação:")
    operacao = input()
    if operacao == "*":
        resultado = n1 * n2
        print ("Resultado é ", resultado)
    elif operacao == "/":
        resultado = n1 / n2
        print ("Resultado é ", resultado)
    elif operacao == "+":
        resultado = n1 + n2
        print ("Resultado é ", resultado)
    elif operacao == "-":
        resultado = n1 - n2
        print ("Resultado é ", resultado)
        funcaoAbertura()
    else:
        calcErro()
        calculadora()

def jogoDaVelha():
    #Coisas para fazer no jogo da velha:
    #printar o tabuleiro, definir as posições em branco
    #E definir a diferença entre o X e O
    #Criar funções dentro de funções, inicialmente criar uma para gerar o tabuleiro
    def explicacaoJogo():
        print("***Jogo da Velha***")
        print("***O jogo da velha é feito para ser jogado por dois jogadores.***\n***O jogador deve escolher um número entre 1 e 9 para definir onde irá jogar(de acordo com a tabela abaixo)***\n")
        print(" 1 | 2 | 3")
        print("===========")
        print(" 4 | 5 | 6")
        print("===========")
        print(" 7 | 8 | 9")

    def proximaJogada(jogadaAnterior, n1, n2, n3, n4, n5, n6, n7, n8, n9):
        if jogadaAnterior == "X":
            jogadaAtual = "O"
        else:
            jogadaAtual = "X"
        iniciarJogo(jogadaAtual,n1, n2, n3, n4, n5, n6, n7, n8, n9)

    def printTabela(n1, n2, n3, n4, n5, n6, n7, n8, n9,jogada):
        limpaTela()
        print(" "+n1+" | "+n2+" | "+n3+"")
        print("===========")
        print(" "+n4+" | "+n5+" | "+n6+"")
        print("===========")
        print(" "+n7+" | "+n8+" | "+n9+"")
        proximaJogada(jogada, n1, n2, n3, n4, n5, n6, n7, n8, n9)

    def iniciarJogo(inicio,n1,n2,n3,n4,n5,n6,n7,n8,n9):
            num = int(input("Digite o local onde irá marcar: " + inicio+"\n"))
        #try:
            
            if num == 1:
                n1 = inicio
            elif num ==2:
                n2 = inicio
            elif num ==3:
                n3 = inicio
            elif num ==4:
                n4 = inicio
            elif num ==5:
                n5 = inicio
            elif num ==6:
                n6 = inicio
            elif num ==7:
                n7 = inicio
            elif num ==8:
                n8 = inicio
            elif num ==9:
                n9 = inicio
            else:
                print("Posição invalida selecionada, tente novamente")
                iniciarJogo(inicio,n1, n2, n3, n4, n5, n6, n7, n8, n9)
            printTabela(n1, n2, n3, n4, n5, n6, n7, n8, n9,inicio)

       # except Exception:
       #    print("Deve ser utilizado números para selecionar a posição onde jogar, digite novamente")
       #   iniciarJogo(inicio)

    def definirVez():
        n1= " "
        n2= " "
        n3= " "
        n4= " "
        n5= " "
        n6= " "
        n7= " "
        n8= " "
        n9= " " 
        print("\n")
        vez = random.randrange(2)
        if vez == 1:
            print("Foi sorteado aleatoriamente X, e ele irá iniciar o jogo")
            iniciarJogo("X",n1, n2, n3, n4, n5, n6, n7, n8, n9)
        else:
            print("Foi sorteado aleatoriamente O, e ele irá iniciar o jogo")
            iniciarJogo("O",n1, n2, n3, n4, n5, n6, n7, n8, n9)
            
    explicacaoJogo()
    definirVez()
   

   
def funcaoAbertura():
    print("Escolha um programa para abrir dentre os listados")
    
    print(" 1 - Calculadora \n 2 - Jogo da velha \n 3 - Caça Niqueis \n 4 - Fechar")
    programa = input("= ")
    if int(programa) == 1:
        limpaTela()
        calculadora()
    elif int(programa) == 2:
        limpaTela()
        jogoDaVelha()
    elif int(programa) == 4:
        return
    else:
        limpaTela()
        print("Valor invalido, digite uma opção valida")
        funcaoAbertura()

#Programa inicia aqui, as funções estão definidas antes do "inicio verdadeiro" do programa
limpaTela()
funcaoAbertura()
# try:
#     if int(x)>=0 and int(x)<=100:
#         print ("O valor digitado foi " + x)
#         limpaTela()
#         funcaoAbertura()
#     else:
#         print("Digitou numero fora do alcance brother")
# except Exception:
#     print("Deu alguma zica ai")
#     print(Exception)

