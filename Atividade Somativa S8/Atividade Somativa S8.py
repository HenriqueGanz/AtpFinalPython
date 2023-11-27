#Nome: Henrique de Godoy Ganz
#Curso: Analise e desenvolvimento de sistemas
#Entrega da Atividade Somativa da Semana 8 Respeitando o Checklist da entrega

#import do modulo JSON
import json

#variavel de armazenamento de dados
cadastro = []
#variavel para loop generico
options = ["ESTUDANTES", "PROFESSORES", "DISCIPLINAS", "TURMAS", "MATRICULAS"]

#Apresentação do Menu Principal
def showMenu():
  print("-----MENU PRINCIPAL-----\n \n (1) Gerenciar Estudantes.\n (2) Gerenciar Professores.\n (3) Gerenciar Disciplinas.\n (4) Gerenciar Turmas.\n (5) Gerenciar Matriculas.\n (6) Sair.")
  selecionarMenu()

#selecao de menu e definicao da variavel de controle (option)
def selecionarMenu():
  opcao = int(input("Qual opção deseja selecionar?\n"))

  if opcao == 1 :
    option = "ESTUDANTES"
    listarOperacoes(option)
  elif opcao == 2 :
    option = "PROFESSORES"
    listarOperacoes(option)
  elif opcao == 3 :
    option = "DISCIPLINAS"
    listarOperacoes(option)
  elif opcao == 4 :
    option = "TURMAS"
    listarOperacoes(option)
  elif opcao == 5 :
    option = "MATRICULAS"
    listarOperacoes(option)
  elif opcao == 6 :
    sair()

#selecao da operacao a realizar
def listarOperacoes(option):
  print(f"-----[{option}] MENU DE OPERACOES-----\n \n (1) Incluir.\n (2) Listar.\n (3) Atualizar.\n (4) Excluir.\n (9) Voltar ao menu principal.")
  resp = int(input("Digite o numero da operação desejada\n"))

  if resp == 1: incluir(option)
  elif resp == 2: listar(option)
  elif resp == 3: atualizar(option)
  elif resp == 4: excluir(option)
  elif resp == 9: showMenu()

#Metodos
#metodo incluir serve para pegar valores de input, recuperar dados e verificar se ja existem na base antes de inserir
def incluir(option):
   #insercao de nome do estudante na lista de estudantes
    print(f"***** Incluir - {option} *****\n") 
    valores = pegarValores(option)
    arquivoRecuperado = recuperarArquivo(option)

    if arquivoRecuperado != "except":
      existe = verificarSeCadastroExiste(valores, arquivoRecuperado)
      if existe == False:
        inserirDados(option, valores, arquivoRecuperado)
      else:
        print("Um cadastro com o mesmo codigo ja existe, use outro codigo")
        listarOperacoes(option)
    else:
      print("nao tem banco de dados, e necessario criar")
      criarBd(option, valores)

    showMenu()

#usado em conjunto de incluir, coleta os dados a serem cadastrados e armazena em seu array antes de transformar em json
def pegarValores(option):
    if option == "ESTUDANTES":
      codigo = input("Digite o codigo do estudante:\n")
      nome = input("Digite o nome do estudante:\n")
      cpf = input("Digite o cpf do estudante:\n")
      valoresEstudante = [codigo, nome, cpf]
      return valoresEstudante
    elif option == "PROFESSORES":
      codigo = input("Digite o codigo do professor:\n")
      nome = input("Digite o nome do professor:\n")
      cpf = input("Digite o cpf do professor:\n")
      valoresProfessor= [codigo, nome, cpf]
      return valoresProfessor
    elif option == "DISCIPLINAS":
      codigo = input("Digite o codigo da disciplina:\n")
      nome = input("Digite o nome da disciplina:\n")
      valoresDisciplina = [codigo, nome]
      return valoresDisciplina
    elif option == "TURMAS":
      codigo = input("Digite o codigo do estudante:\n")
      nomeProfessor = input("Digite o nome do professor:\n")
      codigoDisciplina = input("Digite o codigo da disciplina:\n")
      valoresTurma = [codigo, nomeProfessor, codigoDisciplina]
      return valoresTurma
    elif option == "MATRICULAS":
      codigo = input("Digite o codigo da matricula:\n")
      nomeEstudante = input("Digite o nome do estudante:\n")
      valoresMatricula = [codigo, nomeEstudante]
      return valoresMatricula

#faz a verificacao de codigo, para que nao sejam feitos cadastros duplicados
def verificarSeCadastroExiste(optionValues, arquivoRecuperado):
  #verificar no banco de dados se ja existe o codigo criado, se ja existir retornar true, se nao retornar false
  if arquivoRecuperado != "except":
    existe = False
    for i in arquivoRecuperado:
      if i["codigo"] == optionValues[0]:
        existe = True
        break
    return existe  

#faz a insercao dos dados no Arquivo Json apos preencher a lista
def inserirDados(option, valores, arquivoRecuperado):
    listaPreenchida = preencherDadosNaLista(option, valores, arquivoRecuperado)

    with open(f"{option}.json", "w", encoding="utf-8") as arquivo:
      json.dump(listaPreenchida, arquivo, ensure_ascii=False)
    print("Cadastro realizado")

#Solicitado pela funcao acima, preenche os dados a serem inseridos no Json
def preencherDadosNaLista(option, valores, arquivoRecuperado=None):
  if option == "ESTUDANTES":
      estudante = {
        "codigo": valores[0],
        "nome" : valores[1],
        "cpf" : valores[2]
      }
      if arquivoRecuperado:
        arquivoRecuperado.append(estudante)
      else:
        cadastro.clear()
        cadastro.append(estudante)
  elif option == "PROFESSORES":
    professor = {
      "codigo": valores[0],
      "nome": valores[1],
      "cpf": valores[2]
    }
    if arquivoRecuperado:
      arquivoRecuperado.append(professor)
    else:
      cadastro.clear()
      cadastro.append(professor)
  elif option == "DISCIPLINAS":
    disciplina = {
      "codigo": valores[0],
      "nome": valores[1]
    }
    if arquivoRecuperado:
      arquivoRecuperado.append(disciplina)
    else:
      cadastro.clear()
      cadastro.append(disciplina)
  elif option == "TURMAS":
    turma = {
      "codigo": valores[0],
      "professor": valores[1],
      "codigo":valores[2]
    }
    if arquivoRecuperado:
      arquivoRecuperado.append(turma)
    else:
      cadastro.clear()
      cadastro.append(turma)
  elif option == "MATRICULAS":
    matricula = {
      "codigo": valores[0],
      "estudante": valores[1]
    }
    if arquivoRecuperado:
      arquivoRecuperado.append(matricula)
    else:
      cadastro.clear()
      cadastro.append(matricula)

  if arquivoRecuperado:
    return arquivoRecuperado
  else:
    return cadastro

#faz a Listagem de dados solicitados atraves da funcao pesquisar
def listar(option):
    print(f"***** Listar - {option} *****\n")
    pesquisarDb(option)
    showMenu()

#Edição de dados atraves da variavel de controle
def atualizar(option):
  print(f"***** ATUALIZAR - {option} *****\n")
  codigo = input("Digite o Codigo de qual deseja atualizar: \n")
  listaRecuperada = recuperarArquivo(option)

  for i in listaRecuperada:
    if i["codigo"] == codigo:
      propriedade = input("Digite a propriedade que deseja alterar: \n")
      i[propriedade] = input("Digite o novo: \n")
      print("Dados Atualizados!")
      with open(f"{option}.json", "w", encoding="utf-8") as arquivo:
        json.dump(listaRecuperada, arquivo, ensure_ascii=False)
      print(listaRecuperada)
      gerenciar(option)

#Exclusão de dados atraves da variavel de controle
def excluir(option):
    print(f"***** EXCLUIR - {option} *****\n")
    codigo = input("Digite o Codigo do estudante que deseja excluir: \n")
    with open(f"{option}.json", "r", encoding="utf-8") as arquivo:
      listaRecuperada = json.load(arquivo)

    for i in listaRecuperada:
      if i["codigo"] == codigo:
        listaRecuperada.remove(i)
        print("Excluido com Sucesso!!")
        with open(f"{option}.json", "w", encoding="utf-8") as arquivo:
          json.dump(listaRecuperada, arquivo, ensure_ascii=False)
        print(listaRecuperada)
        showMenu()

#cria o banco de dados caso nao exista
def criarBd(option, valores):
    cadastro = preencherDadosNaLista(option, valores)

    with open(f"{option}.json", "w", encoding="utf-8") as arquivo:
      json.dump(cadastro, arquivo, ensure_ascii=False)
      print("Banco de dados Criado com sucesso")

#faz a pesquisa se o banco de dados existe ou nao tratando o erro com mensagem ao usuario
def pesquisarDb(option):
  try:
    arquivoRecuperado = recuperarArquivo(option)
    print(arquivoRecuperado)
  except:
      return print("Base de dados inexistente")

#recupera os dados da base com tratamento de erro(caso nao exista) com mensagem para o usuario
def recuperarArquivo(option):
  try:
    with open(f"{option}.json", "r", encoding="utf-8") as arquivo:
      cadastrados = json.load(arquivo)
    return cadastrados
  except:
    return "except"

#finaliza a aplicacao se solicitado
def sair():
  return

#Inicio do programa
#funcao que Apresenta o Menu Principal, a partir dele o sistema toma vida.
showMenu()



  
  