#!\bin\python3

lista = []

def add_item():
    print("Informe as informações do item")
    descricao = input("Descrição:")
    preco = input("Preço:")
    item = {
      "descrição":descricao,
      "preço":preco
    }
    lista.append(item)

def lista_itens():
    #lista de item com indice|descrição|preço
    print("Indice|Descrição|Preço")
    print(indice,"|",descricao,"|",preco)
    for item in lista:
        print(item)

def remover_item():
    pass

def informar_preco():
    lista_itens()
    indice = input("Informe o indice:")
    preco = input("Informe o preço:")
    lista[int(indice)]["preço"] = preco

def total_da_lista():
    #retornar total da lista
    pass

def mostrar_menu():
    print("0 - Sair")

while True:
    mostrar_menu()
    opcao = input("Opção:")
    if opcao == "0":
        break
