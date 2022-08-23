
import time as t
import matplotlib.pyplot as plt

#--------------------------------------------------DESCRIÇÃO--------------------------------------------------------------------------------------
def descricao_alg(): #função de descrição do Algoritmo
  print("\t"*3,"####\tEsse algoritmo apresenta um sistema para auxiliar um serviço de Luthiaria especializada em Guitarra!\t####" )
  print("\t"*7," Os serviços prestados são: Regulagem, Blindagem e Pintura." )
#--------------------------------------------------FEEDBACK----------------------------------------------------------------------------------------
def feedback(val): #funcao de feedback das demais funções
  if (val == 1):
    print("\t"*10,"Operação realizada com sucesso!")
    print("")
    t.sleep(2)
  elif (val == 2):
    print("\t"*5,"ATENÇÃO: Não foi possivel realizar a operação! Informação não encontrada!")
    print("")
    t.sleep(2)
#--------------------------------------------------MENU--------------------------------------------------------------------------------------------
def imprime_menus(val):
  if(val == 1):
    print("-"*160)
    print("||","\t"*10, "MENU DE OPÇÕES")
    print("||\t (1) - Cadastrar")
    print("||\t (2) - Buscar")
    print("||\t (3) - Atualizar")
    print("||\t (4) - Remover")
    print("||\t (5) - Listar todos os cadastros")
    print("||\t (6) - Gráficos")
    print("||\t (0) - Sair")
    print("-"*160)
  elif(val == 2):
    print("||", "\t"*10, "GRÁFICOS")
    print("||\t (1) - Quantidade Geral de Serviços")
    print("||\t (2) - Marca-Modelo e Serviços")
    print("||\t (3) - Tipo de Serviço por Marca")
    print("||\t (4) - Quantidade de Modelos por Marca")
    print("||\t (0) - Retornar ao Menu Principal")
    print("-" * 160)


  # ---------------------------------------------------------LEITURA DO ARQUIVO--------------------------------------------]
#--------------------------------------------------LEITURA DO ARQUIVO------------------------------------------------------------------------------
def ler_arq(dic, nome_arq):  # carrega as informações do arquivo num dicionário
    try:
      arq = open(nome_arq, 'r')
    except FileNotFoundError as e:
      arq = open(nome_arq, 'w')
    t.sleep(1.5)
    arq = open(nome_arq, 'r')
    registros = arq.readlines()
    cont = 0
    while (cont < len(registros) // 5):
      dic[registros[5 * cont].strip()] = [registros[5 * cont + 1].strip(), registros[5 * cont + 2].strip(),
                                          registros[5 * cont + 3].strip(),
                                          registros[5 * cont + 4].strip()]  # criando o dicionario com as chaves e valores
      cont += 1
    arq.close()
#--------------------------------------------------CADASTRA----------------------------------------------------------------------------------------
def cadastra(dic):
  nome = input("Nome: ")
  telefone = input("Telefone (somente números): ")
  marca_gt = input("Marca da Guitarra: ")
  modelo_gt = input("Modelo da Guitarra: ")
  tipo_serv = input("Tipo de Serviço: ")
  if telefone not in dic.keys():  #verifica se o telefone não está cadastrado
    dic[telefone] = [nome, marca_gt, modelo_gt, tipo_serv]
  else:
    print("\t"*5,"ATENÇÃO: Não foi possivel realizar a operação. Este telefone já foi cadastrado!")
    print("")
#--------------------------------------------------SALVA NO ARQUIVO-------------------------------------------------------------------------------
def salva_arq(dic, nome_arq):
  arquivo = open(nome_arq, "w")
  for id, info  in dic.items():
    arquivo.write(str(id) + "\n")
    for infos in info:
      arquivo.write(str(infos)+"\n")
  arquivo.close()
  feedback(1)
#--------------------------------------------------BUSCA------------------------------------------------------------------------------------------
def buscar_info(dic, id): #busca informaçoes a partir da chave do dicionario
  if id in dic.keys():
   print("ID (Telefone) ||\t\tNome\t\t ||\t\tMarca\t\t || \t\tModelo\t\t || \t\tServiço")
   print(f' {id:15} {dic[id][0]:20} \t {dic[id][1]:20} \t {dic[id][2]:20} {dic[id][3]:20}') #{:num} determina a quantidade de espaço que a String vai ocupar (tentativa de deixar as info "organizadas")
  else:
    feedback(2)
#--------------------------------------------------LISTA TODOS OS REGISTROS-----------------------------------------------------------------------
def imprime_todas_infos(dic): #imprime todos os registros no dicionario
  print("ID (Telefone) ||\t\tNome\t\t ||\t\tMarca\t\t || \t\tModelo\t\t || \t\tServiço")
  t.sleep(1)
  for chave, valores in dic.items():
    print(f' {chave:15} {valores[0]:25} {valores[1]:20}  {valores[2]:20} {valores[3]:20}')
    print("-"*160)
    print("")
    t.sleep(0.5)
#--------------------------------------------------ATUALIZA----------------------------------------------------------------------------------------
def atualiza_info(dic, id): #atualiza atributos a partir da chave do dicionario
  if id in dic.keys():
   print("Os dados escolhidos para serem alterados foram: ")
   buscar_info(dic, id)
   print("-"*120)
   nome = input("Nome: ")
   marca_gt = input("Marca da Guitarra: ")
   modelo_gt = input("Modelo da Guitarra: ")
   tipo_serv = input("Tipo de Serviço: ")
   dic[id] = [nome, marca_gt, modelo_gt, tipo_serv]
   salva_arq(dic, "banco_luthier.txt")
  else:
    feedback(2)
#--------------------------------------------------REMOVE------------------------------------------------------------------------------------------
def remove_info(dic, atrib): #função remove informação a partir da chave
  l_valores = []
  l_chaves = []
  l_modelo = []
  for chave, valores in dic.items():
    if atrib in valores:
      l_chaves += [chave]
      l_valores += [valores]
      l_modelo += [valores[2]]
  if (l_modelo.count(atrib) == 1):
   dic.pop(l_chaves[0])
   salva_arq(dic, "banco_luthier.txt")
  elif (l_modelo.count(atrib) > 1):
    print("-"*160)
    print("\tHá mais de um registro com o Modelo da Guitarra informado!")
    print("\tSerá exibido os telefones, nome e serviço realizado com o modelo inserido!")
    print("\tInforme o telefone do cliente que deseja remover!")
    print("-"*160)
    for chaves, valores in zip(l_chaves, l_valores):
      print("\tTelefone: ",chaves, "|| Nome: ", valores[0],"|| Serviço: ", valores[3])
      print("-"*160)
    telefone = input("Telefone: ")
    dic.pop(telefone)
    salva_arq(dic, "banco_luthier.txt")
  else:
    feedback(2)
#--------------------------------------------------PIE CHARTS GERAL DOS SERVIÇOS-------------------------------------------------------------------
def gera_grafico_serv(dic):
  y = []
  pintura = blindagem = regulagem = 0
  for valores in dic.values():
    if 'Pintura' in valores:
      pintura +=1
    elif 'Blindagem' in valores:
      blindagem +=1
    elif 'Regulagem' in valores:
      regulagem +=1

  y = [blindagem, regulagem, pintura]
  mylabels = ['Blindagem', 'Regulagem', 'Pintura']
  plt.pie(y, labels = mylabels, shadow = True)
  plt.title('Quantidade de Serviço \n Visão Geral')
  plt.legend()
  plt.show()
#--------------------------------------------------SCATTER MARCA X MODELO E TIPO DE SERVIÇO (VISÃO GERAL)-----------------------------------------
def gera_grafico_scatter(dic):
  lista_marca = []
  lista_serv = []
  for valores in dic.values(): 
    lista_marca += [valores[1]+' '+valores[2]]
    lista_serv += [valores[3]]
  plt.scatter(lista_serv, lista_marca, color='orange')
  plt.title('Marca-Modelo X Tipo de Serviço \n Visão Geral')
  plt.ylabel('Marca-Modelo')
  plt.xlabel('Serviço')
  plt.grid(axis='y',linestyle='solid', alpha = .1,  color='royalblue')
  plt.show()
#--------------------------------------------------HIST DA QUANTIDE DE SERVIÇO POR MARCA----------------------------------------------------------
def gera_grafico_marca(dic, marca):
  lista_serv = []
  for valores in dic.values():
    if valores[1] == marca:
      lista_serv += [valores[3]]

  plt.hist(lista_serv, ec = "k", alpha = .6, color = "royalblue") #ec = cor das bordas das barras, alpha = transparencia
  plt.title(f'Quantidade do Tipo de Serviço por Marca \n\n {marca}')
  plt.ylabel('Quantidade')
  plt.xlabel('Serviço')
  plt.show()
#--------------------------------------------------HIST DOS MODELOS POR MARCA---------------------------------------------------------------------
def gera_grafico_modelo_marca(dic, marca):
  lista_modelos = []
  for valores in dic.values():
    if valores[1] == marca:
      lista_modelos += [valores[2]]
  lista_modelos.sort()

  plt.hist(lista_modelos, ec = "k", alpha = .6, color = "royalblue") #ec = cor das bordas das barras, alpha = transparencia
  plt.title(f'Quantidade de Modelos por Marca \n\n {marca}')
  plt.ylabel('Quantidade')
  plt.xlabel('Modelo')
  plt.show()

#----------------------------------------------------MAIN-----------------------------------------------------------------------------------------
print("-"*160)
dic_luthiaria = {}

ler_arq(dic_luthiaria, "banco_luthier.txt") #leitura do arquivo para carregar as informações no dicionario para serem manipuladas na execução do algoritmo
descricao_alg()

op = -1
while (op != 0 ):
  imprime_menus(1)
  op = int(input("Informe o numero da operação a ser realizada: "))
  print("-"*160)
  if (op == 1): 
    cadastra(dic_luthiaria)
    salva_arq(dic_luthiaria, "banco_luthier.txt")
  elif (op == 2):
    telefone = input("Informe o numero de telefone para BUSCAR as informações sobre o cliente: ")
    buscar_info(dic_luthiaria, telefone)
    print("-"*160)    
  elif (op == 3):
    telefone = input("Informe o numero de telefone para ATUALIZAR as informações sobre o cliente: ")
    atualiza_info(dic_luthiaria, telefone)
  elif (op == 4):
    telefone = input("Informe o modelo da guitarra para REMOVER as informações sobre o cliente: ")
    remove_info(dic_luthiaria, telefone)
    print("-"*160) 
  elif (op == 5):
    imprime_todas_infos(dic_luthiaria)
  elif (op == 6):
    op2 = -1
    while(op2 != 0):
      imprime_menus(2)
      op2 = int(input("Informe o numero da opção desejada: "))
      if(op2 == 1):
        gera_grafico_serv(dic_luthiaria)
      elif(op2 == 2):
        gera_grafico_scatter(dic_luthiaria)
      elif(op2 == 3):
        marca = input("Informe a marca para visualizar os serviços: ")
        gera_grafico_marca(dic_luthiaria, marca)
      elif (op2 == 4):
        marca = input("Informe a marca para visualizar os modelos: ")
        gera_grafico_modelo_marca(dic_luthiaria, marca)

print("Encerrando o algoritmo...")
t.sleep(1.5)
print("Encerrado!")
