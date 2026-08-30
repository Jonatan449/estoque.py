from time import sleep
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
        pro["nome"]=input("Produto que deseja cadastrar: ")
        pro["valor"]=float(input("Valor do produto: "))
        pro["quantidade"]=int(input("Quantos produtos: "))
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
                  
           
while True:
    print(f"{'ESTOQUE':=^35}")
    print("""
    [1]Cadastrar produtos
    [2]Listar produtos
    [3]Buscar produtos
    [4]Alterar quantidade
    [5]Remover produto
    [6]Sair""")
    linha()
    while True:
        try:
           option=int(input(f"{cores['amarelo']}Digite sua escolha: {cores['limpa']}"))
           while option not in[1,2,3,4,5,6]:
                  option=int(input("Tente novamente: "))
           break
        except:
           print(f"{cores['vermelho']}ERRO: digite apenas números inteiros\nNão use letras ou números decimais{cores['limpa']}")
           
    linha()
    if option==1:
           cadastrar()
    elif option==2:
           if not produtos:
                  print("Não há produto cadastrado.")
           for produto in produtos:
                  print(f'{produto["nome"]} — R${produto["valor"]:g} — {produto["quantidade"]} unidades')
    elif option==3:
           buscar()
    elif option==4:
           alt_quant=input("Deseja alterar a quantidade de qual produto: ").strip().casefold()
           achou=False
           for produto in produtos:
                  if produto["nome"].casefold()==alt_quant:
                         print(f"Sua quantidade atual é {cores["verde"]}{produto['quantidade']}{cores['limpa']}\n")
                         achou=True
                         while True:
                                try:
                                    novo_numero=int(input("Nova quantidade do produto: "))
                                    break
                                except ValueError:
                                    print(f"{cores['vermelho']}ERRO: digite apenas números inteiros\nNão use letras ou números decimais{cores['limpa']}")
                         produto["quantidade"]=novo_numero
                         print("\nAtualizando...")
                         sleep(1)
                         print(f"{cores["verde"]}Atualizado!\nO produto '{produto["nome"]}' agora\ntem {produto["quantidade"]} unidades{cores["limpa"]}")
           if not achou:
                  print(f"{cores['amarelo']}Não achei produto cujo nome é '{alt_quant}'\nVerifique e tente novamente.{cores['limpa']}")
    elif option==5:
           crtz=input("Tem certeza que deseja excluir?\n[S/N]: ").strip().lower()
           if crtz=="s":
               exc=input("Qual produto deseja excluir: ").strip().casefold()
               achou=False
               for produto in produtos:
                      if produto["nome"].casefold()==exc:
                             produtos.remove(produto)
                             print("Produto deletado com sucesso.")
                             achou=True
                             break
               if not achou:
                      print(f"{cores['branco']}Não encontramos '{exc}' para excluir\nVerifique o nome e tente novamente.{cores['limpa']}")
    elif option==6:
           print("Ok, tchau")
           break