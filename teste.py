import json

n = input("Digite o seu nome: ")
l = input("Digite o seu level: ")


#Para ler o arquivo json
with open("seleções.json", "r") as arq:
    dados = json.load(arq)

#Para adicionar coisas
novo_jogador = {"nome": n,"nivel": l }
dados["s"].append(novo_jogador)

with open("seleções.json", "w") as arq:
    json.dump(dados, arq, indent=4, ensure_ascii=False)

while True:

    r = input("editar?")
    if r in "Ss":
        n_procurado = input("Qual Jogador?")
        l_novo = input("Diga o novo level")
    elif r in "Nn":
        break

    for jogador in dados["s"]:
        if jogador["nome"] == n_procurado:
            jogador["nivel"] = l_novo
            print("Level Atualizado")
            break
        else:
            print("Jogador não encontrado")

with open("seleções.json", "w") as arq:
    json.dump(dados, arq, indent=4, ensure_ascii=False)

