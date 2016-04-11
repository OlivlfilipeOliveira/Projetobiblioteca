#----------------------------------------------------------------------------------------------#
#--------------------------IFAL-Campus Palmeira dos Índios-------------------------------------#
#----------------------Autores: Filipe Olveira e Yuri Pereira----------------------------------#
#----------------------------Disciplina: ESTRURA DE DADOS--------------------------------------#
#------------------------------Professor: Emerson Lima-----------------------------------------#
#-------------------------------Título: BIBLIOTECA---------------------------------------------#
#-------------------------------Inicio: 21/03/2016---------------------------------------------#
#-------------------------------Fim: 31/03/2016------------------------------------------------#
#----------------------------------------------------------------------------------------------#

import os #A biblioteca 'os' vai importar um método que vai limpar a tela, no momento que for chamado.
import time #A biblioteca 'time' vai importar um método pra determinar um tempo na execução do programa, no momento que for chamado.

alunos = [["Zé","123456",[]],["Biu","123657",[]],["Elk","809654",[]]]
#Lista que contém os alunos e seus respctivos cadastrados.
livros = [["a moreninha","Não emprestado"],["príncipe","Não emprestado"],["dom casmurro","Não emprestado"]]
#Lista que contém os livros disponiveis e os não disponiveis.

#1ª função. Ela realiza o cadastro dos alunos.
def cadastro_alunos():          
    nome = input("Nome: ")
    matricula = input("Matrícula(6 DIGITOS): ")
    if(len(matricula)<6) or (len(matricula)>6): #Verificação da matrícula (válida/inválida).
        print("Matrícula inválida!")
        return "O cadastro foi cancelada!"
    else:
        verifiq = 0
        for i in range(len(alunos)): #Verificação da matrícula (cadastradaa/não cadastrada).
            if(matricula in alunos[i]):
                verifiq = 1
                break
        if(verifiq==1):
            print("Informe uma matrícula que não esteja cadastrada no sistema! ")
            return "O cadastro foi cancelado!"
        else:
            pergunt = input("Já pegou algum livro emprestado (sim/não): ")
            if(pergunt=="sim"):
                livrosEmprest = input("Informe o(s) livro(s) emprestado(s)(separe os livros por vírgula): ")
                livrosEmprest = livrosEmprest.split(",")
            else:
                livrosEmprest = []
            alunos.append([nome,matricula,livrosEmprest])
            return "Cadastro do aluno efetivado!"
            
#2ª função. Ela realiza o cadastro dos livros.
def cadastro_livros():
    título = input("Nome do livro: ")
    título = título.lower()    #O método 'lower' transforma qualquer tipo string maiuscula em minúscula,(em todos os casos).
    status = "Não emprestado"
    livros.append([título,status])
    return "Cadastro do livro efetivado"

#3ª função. A qual realiza os emprestimos de livros e faz suas respctivas operações.
def emprestimos():
    matricula = input("Matrícula(6 DIGITOS): ") 
    if(len(matricula)<6) or (len(matricula)>6):   #Verificação da matrícula (válida/inválida).
        print("Matrícula inválida!")
        return "O emprestimo foi cancelado!"
    else:
        verifiq = 0 #'verifiq' é uma variável verificadora em todos os casos que ela é definida.
        for i in range(len(alunos)): #Verificação da matrícula (cadastradaa/não cadastrada).
            if(matricula==alunos[i][1]):
                verifiq = 1
        if(verifiq!=1):
            print("Informe uma matrícula que esteja cadastrada no sistema! ")
            return "O emprestimo foi cancelado!"
        else:
            título = input("Título do livro: ")
            título = título.lower()
            verifiq = 0
            #Este 'for'(Estrutra de repetição), irá verficiar se o livro é valido ou não, para realizar a devida operação.
            for i in range(len(livros)):
                if(título in livros[i]):
                    verifiq = 1
                    break
            if(verifiq!=1):
                print("O livro que você solicitou não está no sistema!")
                return "O emprestivo foi cancelado!"
            else:
                verifiq = 0
                #Este 'for'(Estrutra de repitição),irá verificar se o livro está dispinível no sistema, para realizar a devida operação.
                for i in range(len(livros)):
                    if(título == livros[i][0]) and (livros[i][1]=="Não emprestado"):
                        livros[i][1] = "Emprestado"
                        verifiq=1
                        aux = [] #'aux' é uma lista auxiliar (em todos os casos que ela é definida).
                        for j in range(len(alunos)):
                            if(matricula in alunos[j]):
                                aux = alunos[j][2]
                                aux.append(título)
                                break
                        return "O emprestimo foi realizado!"
                if (verifiq !=1):
                    return "O livro não está disponível!"
                
#4ª função. Realiza a devolução dos livros.
def devolução():
    matricula = input("Matrícula(6 DIGITOS): ")
    if((len(matricula)<6) or (len(matricula)>6)):
        print("Matrícula inválida!")
        return "A devolução foi cancelada!"
    else:
        #Esse 'for' irá verificar uma matricula existente, para poder realizar a devolução do livro.
        verifiq = 0 #'verifiq' é uma vareiável verificadora(obs.:em todos os casos).
        for i in range(len(alunos)):
            if(matricula==alunos[i][1]):
                verifiq = 1
                break
        if(verifiq!=1):
            print("Informe uma matrícula que esteja cadastrada no sistema! ")
            return "A devolução foi cancelada!"
        else:
            título = input("Título do livro: ")
            título = título.lower()
            verifiq = 0
            #Esse 'for' irá verificar se o que usuário  informou está no sistema ou não.
            for i in range(len(livros)):
                if(título in livros[i]):
                    verifiq = 1
                    break
            if(verifiq!=1):
                return "O livro que você informou não está no sistema! "
            else:
                verifiq = 0
                for i in range(len(livros)):
                    if((título == livros[i][0]) and (livros[i][1]=="Emprestado")):
                        livros[i][1] = "Não emprestado"
                        verifiq = 1
                        
                        aux = 0
                        j = 0
                        while(j<len(alunos)):   #Esse comando 'while' irá confirmar a devolução do livro.
                            if(título in alunos[j][2]):
                                aux = alunos[j][2]
                                aux.remove(título)
                                break
                            j += 1
                        return "A devolução foi realizada!"
                if(verifiq!=1):
                    return "O livro não está no seu cadastro!"
        
#5ª função. Ela mostrará os alunos cadastrados no sistema.
def listagem_alunos():
    print("\n")
    for i in range(len(alunos)):
        print(alunos[i][0])
    return ""

#6ª função. Ela mostrará os livros cadastrados no sistema.
def listagem_livros():
    print("\n")
    for i in range(len(livros)):
        print(livros[i][0])
    return ""

#A partir daqui começa o código principal.
#Esse código principal tem como objetivo chamar todas as funções definidas acima.
while(True):
    print("|-----------------------------------------------------------|")
    print("                        BIBLIOTECA                         ")
    print("|-----------------------------------------------------------|\n")
    print("""
                  1-Cadastar alunos
                  2-Cadastrar livros
                  3-Fazer emprestimos
                  4-Devolução de livros
                  5-Listagem de alunos
                  6-Listagem de livros
                  7-Sair
        """)
    print("|-----------------------------------------------------------|")

    op = input("\nInforme a opção desejada(nº): ")
    opção = int(op)
    if(opção==1):
        print(cadastro_alunos())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção==2):
        print(cadastro_livros())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção==3):
        print(emprestimos())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção==4):
        print(devolução())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção==5):
        print(listagem_alunos())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção==6):
        print(listagem_livros())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção==7):
        print("Você saiu...")
        time.sleep(3)
        break
    else:
        print("Opção inválida!")
        print("Enter para contnuar...")
        input()
        os.system("Cls")
        continue
