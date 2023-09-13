import json

compras = {}

def adicionar_item(compras, item, quantidade):
    compras[item] = quantidade

def remover_item(compras, item):
    if item in compras:
        del compras[item]
    

def visualizar_compras(compras):
    for item, quantidade in compras.items():
        print(f"{item}: {quantidade}")
    print()
    print("Pressione enter para continuar")
    input()

def salvar_compras(compras, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(compras, arquivo)

def carregar_compras(nome_arquivo):
    with open(nome_arquivo.json, "r") as arquivo:
        return json.load(arquivo)

def gerenciar_compras(compras):
    pass

def main():
    pass

adicionar_item(compras,"arroz", 2)
remover_item(compras,"arroz")
print(compras)