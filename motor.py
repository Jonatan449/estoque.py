produtos=[]
cores={"amarelo": "\033[1;33m",
       "vermelho": "\033[1;31m",
       "branco": "\033[1;97m",
       "azul": "\033[1;34m",
       "ciano": "\033[1;36m",
       "roxo": "\033[1;35m",
       "cinza": "\033[1;37m",
       "verde": "\033[1;32m",
       "limpa": "\033[m"}
def cadastrar():
    pro={}
    while True:
        try:
            quant=int(input("Quantos produtos: "))
            break
        except ValueError:
            print(f"{cores['vermelho']}ERRO: digite apenas números inteiros\nNão use letras ou números decimais{cores['limpa']}\n")
        except KeyboardInterrupt:
            print("PROGRAMA ENCERRADO")
            exit()
    for a in range(quant):
        a+=1
        print(f"\n{cores['azul']}Produto {a}:{cores['limpa']}")
        while True:
               pro["nome"]=input("Produto que deseja cadastrar: ").strip().casefold()
               repetido=False
               for produto in produtos:
                      if produto['nome']==pro['nome']:
                             repetido=True
                             break
               if repetido:
                      print(f'{cores["vermelho"]}JÁ EXISTE UM PRODUTO COM ESSE NOME!!{cores["limpa"]}')
                      continue
                             
               if not repetido:
                             break
        while True:
               try:
                  pro["valor"]=float(input("Valor do produto: "))
                  break
               except:
                  print(f"{cores['vermelho']}DIGITE APENAS NÚMEROS\nNÃO COLOQUE LETRAS OU SIMBOLOS{cores['limpa']}")
        while True:          
               try:
                  pro["quantidade"]=int(input("Quantos produtos: "))
                  break
               except:
                  print(f"{cores['vermelho']}Digite apenas números INTEIROS\nNÃO coloque LETRAS, SIMBOLOS ou \nNÚMEROS DECIMAIS{cores['limpa']}")
        print(f'{cores["azul"]}~{cores["limpa"]}'*35)
        produtos.append(pro.copy())
        pro.clear()
def linha():
    print(f"_"*20)
def buscar():
    p=0
    print("""
    [1]Buscar pelo nome
    [2]Buscar pela quantidade
    [3]Buscar pelo preço""")
    linha()
    while True:
           try:
              escolha=int(input("Sua escolha: "))
              while escolha not in [1,2,3]:
                     escolha=int(input("Tente novamente(1,2,3): "))
              break
           except ValueError:
              print(f"{cores['vermelho']}ERRO: digite apenas números inteiros\nNão use letras ou números decimais{cores['limpa']}")
    linha()
    if escolha==1:
           nome=input(f"{cores['roxo']}Digite o nome do produto: {cores['limpa']}").strip().casefold()
           encontrou=False
           for produto in produtos:
                  if produto["nome"].casefold()==nome:
                         p+=1
                         print(f'{cores["ciano"]}Produto {p}:{cores["limpa"]}')
                         print(f"{cores["verde"]}Nome:{cores["limpa"]}{produto["nome"]}\n{cores["verde"]}Preço: {cores["limpa"]}R${produto['valor']:g}\n{cores["verde"]}Unidades: {cores["limpa"]}{produto['quantidade']:g}{cores["limpa"]}\n")
                         encontrou=True
           if not encontrou:
                  print(f'{cores["vermelho"]}Não foi encontrado produtos\nrelacionado a "{nome}"{cores["limpa"]}')
    elif escolha==2:
           while True:
                  try:
                     quant=int(input(f'{cores["roxo"]}Digite a quantidade de itens: {cores["limpa"]}'))
                     break
                  except ValueError:
                     print(f"{cores['vermelho']}ERRO: digite apenas números inteiros\nNão use letras ou números decimais{cores['limpa']}\n")
           achou=False
           for produto in produtos:
                  if produto["quantidade"]==quant:
                         p+=1
                         print(f"{cores["ciano"]}Produto {p}:{cores["limpa"]}")
                         print(f'{cores["verde"]}Unidades: {cores["limpa"]}{quant:g}\n{cores["verde"]}Preço: {cores["limpa"]}R${produto["valor"]:g}\n{cores["verde"]}Nome: {cores["limpa"]}{produto["nome"]}\n')
                         achou=True
           if not achou:
                  print(f"{cores['vermelho']}Não foi possível encontrar produtos com {quant} unidades.\nVerifique a quantidade e tente\nnovamente{cores['limpa']}")
    elif escolha==3:
           while True:
                  try:
                     preco=float(input("Digite o valor do item: "))
                     break
                  except ValueError:
                     print(f"{cores['vermelho']}ERRO: digite apenas números\nEvite letras, símbolos($,%,..),\nespaços ou qualquer outra coisa\nalém de números{cores['limpa']}")
           achou=False
           for produto in produtos:
                  if produto["valor"]==preco:
                         p+=1
                         print(f"{cores['ciano']}Produto {p}: {cores['limpa']}")
                         print(f'{cores["verde"]}Preço: {cores["limpa"]}R${preco:g}\n{cores["verde"]}Nome: {cores["limpa"]}{produto["nome"]}\n{cores["verde"]}Unidades: {cores["limpa"]}{produto["quantidade"]}\n')
                         achou=True
           if not achou:
                  print(f"{cores['vermelho']}Não foi possível encontrar produtos com R${preco:g}.\nVerifique o preço e tente\nnovamente{cores['limpa']}")
