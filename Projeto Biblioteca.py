#----------------------------------------------------------------------------------------------#
#--------------------------IFAL-Campus Palmeira dos Índios-------------------------------------#
#----------------------Autores: Filipe Olveira e Yuri Pereira----------------------------------#
#----------------------------Disciplina: ESTRURA DE DADOS--------------------------------------#
#------------------------------Professor: Emerson Lima-----------------------------------------#
#-------------------------------Título: BIBLIOTECA---------------------------------------------#
#-------------------------------Inicio: 21/03/2016---------------------------------------------#
#-------------------------------Fim: 20/04/2016------------------------------------------------#
#----------------------------------------------------------------------------------------------#
import os #A biblioteca 'os' vai importar um método que vai limpar a tela, no momento que for chamado.
import time #A biblioteca 'time' vai importar um método pra determinar um tempo na execução do programa, no momento que for chamado.

aluno = open("alunos.txt","r")#Vai ler o arquivo 'alunos' e irá transferir os dados para a lista alun.
alun = aluno.readlines()
livro = open("livros.txt","r")#Vai o arquivo 'livros' e irá transferir os dados para a lista 'livr'.
livr = livro.readlines()
aluno.close()
livro.close()
#O bloco de instrução abaixo vai transferir os dados lista 'alun' gerada pelo comando 'readlines', e serão
#armazenados em uma matriz chamada 'alunos'.
alunos = []
for i in alun:
    i = i.split("#") #Este comando vai fazer com que os dados do aluno seja separados por "#", (em todos os casos).
    i.remove("\n")#Este comando vai remover os "\ns" desnecessários porque não serão utilizados na consulta(em todos os casos).
    alunos.append(i)

#Este outro bloco de instrução vai fazer a mesma coisa que o primeiro, porém agora vai transferir os dados para matriz 'livros'.
livros = []
for s in livr:
    s = s.split("#")
    s.remove("\n")
    livros.append(s)

#A função abaixo, ficará encarregada de atualizar os arquivos 'livros' e 'alunos'.
def arquivos():
    global aluno,livro,alunos,livros
    aluno = open("alunos.txt", "w")
    livro = open("livros.txt","w")

    for i in range(len(alunos)): #Vai adicíonar os novos alunos cadstrados no arquivo, e dando uma quebra de linha para facilitar a utilização dos mesmo.
        for j in range(len(alunos[i])):
            aluno.write("%s#" % alunos[i][j])
        aluno.write("\n")
    for l in range(len(livros)): #Vai adicíonar os novos livros cadstrados no arquivo, e dando uma quebra de linha para facilitar a utilização dos mesmo.
        for i in range(len(livros[l])):
            livro.write("%s#" % livros[l][i])
        livro.write("\n")
    aluno.close() #fecamento do arquivo.
    livro.close() #fechamento do arquivo.

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
            #Esse bloco de instrução permite ao aluno fazer o emprestimo do livro durante seu cadastro na biblioteca.
            #Caso sua resposta seja 'sim'.
            pergunt = input("Você quer pegar algum livro emprestado (sim/não): ")
            if(pergunt=="sim"):
                alunos.append([nome,matricula])
                livrosEmprest = input("Informe o(s) livro(s) que você quer pegar emprestado(s)(separe os livros por vírgula): ")
                livrosEmprestados = livrosEmprest.split(",")
                for i in range(len(livrosEmprestados)): #Essa estrutura de repetição irá verificar se o livro desejado está disponível ou não.
                    livrosEmprestados[i] = livrosEmprestados[i].lower()
                    verifiq = 0
                    v = 0
                    for j in range(len(livros)):
                        if((livrosEmprestados[i]==livros[j][0]) and (livros[j][1]=="Não emprestado")):
                            aux = [] #'aux' é uma lista auxiliar (em todos os casos que ela é definida).
                            for x in range(len(alunos)):
                                if(matricula in alunos[x]):
                                    verifiq = 1
                                    livros[j][1] = "Emprestado"
                                    aux = alunos[x]
                                    aux.append(livrosEmprestados[i])
                                    print("O emprestimo do livro %s foi realizado!" % livrosEmprestados[i])
                                    break
                    if(verifiq==0):
                        print("O livro %s não está disponível!" % livrosEmprestados[i])
            else:
                alunos.append([nome,matricula])
            arquivos()
            return "Cadastro do aluno efetivado!"

#2ª função. Ela realiza o cadastro dos livros.
def cadastro_livros():
    título = input("Nome do livro: ")
    título = título.lower()    #O método 'lower' transforma qualquer tipo string maiuscula em minúscula,(em todos os casos).
    status = "Não emprestado"
    livros.append([título,status])
    arquivos()
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
                                aux = alunos[j]
                                aux.append(título)
                                break
                        arquivos()
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
                for i in range(len(livros)): #Essa função irá verificar se o titulo do livro que deseja devolver corresponde com a de quem o pegou.
                    if((título == livros[i][0]) and (livros[i][1]=="Emprestado")):
                        for x in range(len(alunos)):
                            if((título in alunos[x]) and (alunos[x][1]!=matricula)):#Verificará se a matricula que o usúario corresponde com a de quem solicitou o livro.
                                return "A matrícula não corresponde com o emprestimo!"
                        livros[i][1] = "Não emprestado"
                        verifiq = 1
                        aux = 0
                        j = 0
                        while(j<len(alunos)):   #Esse comando 'while' irá confirmar a devolução do livro.
                            if(título in alunos[j]):
                                aux = alunos[j]
                                aux.remove(título)
                                break
                            j += 1
                        arquivos()
                        return "A devolução foi realizada!"
                if(verifiq!=1):
                    return "O livro não está no seu cadastro!"

#5ª Função, vai remover o cadastro de um aluno do sistema.
def remover_aluno():
    matricula = input("Matrícula(6 DIGITOS): ")
    if(len(matricula)<6) or (len(matricula)>6):   #Verificação da matrícula (válida/inválida).
        print("Matrícula inválida!")
        return "O remoção do cadastro foi cancelada!"
    else:
        verifiq = 0 #'verifiq' é uma variável verificadora em todos os casos que ela é definida.
        for i in range(len(alunos)): #Verificação da matrícula (cadastradaa/não cadastrada).
            if(matricula==alunos[i][1]):
                verifiq = 1
        if(verifiq!=1):
            print("Informe uma matrícula que esteja cadastrada no sistema! ")
            return "A remoção do cadastro foi cancelada!"
        else:
            for i in range(len(livros)):
                for j in range(len(alunos)):
                    if((livros[i][0] in alunos[j]) and (matricula==alunos[j][1])): #Essa função irá verificar se o aluno tem livro, caso sim ele vai alterar o status do livro que o aluno pegou para "Não-emprestado"
                        livros[i][1] = "Não emprestado"
            for x in range(len(alunos)):
                if(matricula in alunos[x]):
                    del alunos[x] #Vai deletar o aluno da posição "x" do arquivo.
                    arquivos()
                    return "A remoção do cadastro foi realizada!"

#6ª Função. vai alterar o nome de um determinado livro que esteja no sistema.
def alterar_livro():
    título = input("Título do livro: ")
    título = título.lower()
    verifiq = 0
    for i in range(len(livros)):
        if(título in livros[i]):
            novo_título = input("Informe o novo nome do livro: ")#Vai receber o novo titulo do livro para que possa ser alterado.
            novo_título = novo_título.lower()
            livros[i][0] = novo_título
            for j in range(len(alunos)):
                #Caso o livro alterado esteja emprestado o sistema se encarregará de altera-lo onde quer que ele esteja.
                for x in range(len(alunos[j])):
                    if(título==alunos[j][x]):
                        alunos[j][x] = novo_título
            verifiq = 1
            arquivos()
            return "Alteração realizada!"
    if(verifiq==0):#Caso o livro não exista, o processo é cancelado.
        return "O livro informado não existe no sitema!"

#7ª função. Ela mostrará os alunos cadastrados no sistema.
def listagem_alunos():
    print("\n")
    if(len(alunos)==0):
        return "Nenhum aluno cadastrado no sistema!\n"
    for i in range(len(alunos)):
        print(alunos[i][0])
    return ""

#8ª função. Ela mostrará os livros cadastrados no sistema.
def listagem_livros():
    print("\n")
    if(len(livros)==0):
        return "Nenhum livro cadastrado no sistema!\n"
    for i in range(len(livros)):
        print("%s: %s" % (livros[i][0],livros[i][1]))
    return ""

#A partir daqui começa o código principal.
#Esse código principal tem como objetivo chamar todas as funções definidas acima.
while(True):
    print("|-----------------------------------------------------------|")
    print("                        BIBLIOTECA                         ")
    print("|-----------------------------------------------------------|\n")
    print("""
                  1-Cadastrar alunos
                  2-Cadastrar livros
                  3-Fazer emprestimos
                  4-Devolução de livros
                  5-Remoção de cadastro de um aluno
                  6-Alterar cadastro de um livro
                  7-Listagem de alunos
                  8-Listagem de livros
                  9-Sair
        """)
    print("|-----------------------------------------------------------|")

    opção = input("\nInforme a opção desejada(nº): ")
    if(opção=="1"):
        print(cadastro_alunos())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção=="2"):
        print(cadastro_livros())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção=="3"):
        print(emprestimos())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção=="4"):
        print(devolução())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção=="5"):
        print(remover_aluno())
        print("Enter para continuar...")
        input()
        os.system("Cls")
    elif(opção=="6"):
        print(alterar_livro())
        print("Enter para continuar...")
        input()
        os.system("Cls")
    elif(opção=="7"):
        print(listagem_alunos())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção=="8"):
        print(listagem_livros())
        print("Enter para contnuar...")
        input()
        os.system("Cls")
    elif(opção=="9"):
        print("Você saiu...")
        time.sleep(3)
        break
    else:
        print("Opção inválida!")
        print("Enter para contnuar...")
        input()
        os.system("Cls")
        continue
