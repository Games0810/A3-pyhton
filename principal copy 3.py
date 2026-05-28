import json
from random import randint
from funções import texto
from funções import numeros



while True:
    print("""
Bem vindo, escolha uma das coisas a seguir:
1- Ver lista
2- Ver o cadastro de um país
3- Adicionar
4- Excluir
5- Editar
6- Sair""")
    while True:
            escolha = input("Resposta: ")

            if numeros(escolha):
                escolha = int(escolha)
                break

    if escolha not in (1,2,3,4,5,6):
        print("Escolha um número na lista")

    with open("seleções.json", "r") as arq:
        dados = json.load(arq)

    if escolha == 1:
        print("-="*20)
        for lista in dados["s"]:
            print(f"ID: {lista['ID']}")
            print(f"País: {lista['País']}")
            print(f"Grupo: {lista['Grupo']}")
            print(f"Confederação: {lista['Confederação']}")
            print(f"Treinador: {lista['Treinador']}")
            print("-="*20)

    elif escolha == 2:
        while True:
            encontrado3 = False
            lista_nome = input("Fale o ID do país: ")

            if numeros(lista_nome):
                lista_nome = int(lista_nome)
                break

        for p in dados["s"]:
            if p["ID"] == lista_nome:
                    encontrado3 = True
                    print("-="*20)
                    print(f"ID: {p['ID']}")
                    print(f"País: {p['País']}")
                    print(f"Grupo: {p['Grupo']}")
                    print(f"Confederação: {p['Confederação']}")
                    print(f"Treinador: {p['Treinador']}")
                    print("-="*20)
        if encontrado3 == False:
            print("País não encontrado")


    elif escolha == 3:
        id_criado = False
        duplicado = False
        while True:
            novo_id = ""
            id = ""
            s = ""
            for i in range (10):
                n = randint(1,9)
                s += str(n)
                id = int(s)
            for ids in dados["s"]:
                if id == ids["ID"]:
                    duplicado = True
                    continue

                if not duplicado:
                    novo_id = id
                    id_criado = True
                    break

            if id_criado == True:
                break 

        while True:
            novo_p = input("País: ")

            if texto(novo_p):
                break
        
        while True:
            novo_g = input("Grupo: ").strip()

            if novo_g == "":
                print("Não pode digitar nada")
                continue
            else:
                break

        while True:
            novo_c = input("Confederação: ")

            if texto(novo_c):
                break

        while True:
            novo_t = input("Treinador: ")

            if texto(novo_t):
                break

        nova_seleção = {"País": novo_p, "Grupo": novo_g, "Confederação": novo_c, "Treinador": novo_t, "ID": int(novo_id)}
        dados["s"].append(nova_seleção)

        with open("seleções.json", "w") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
    
    elif escolha == 4:
        encontrado = False
        while True:
            remover = input("Fale o ID do país: ").strip()

            if numeros(remover):
                remover = int(remover)
                break 

        for lista in dados["s"]:
            if lista["ID"] == remover:
                print("ID encontrado")
                encontrado = True
                if encontrado == True:
                        while True: 
                            confirmacao = input(f"Você realmente desejar excluir os dados do país {lista["País"]}? [S/N]").upper().strip()
                            
                            if confirmacao == "S":
                                dados["s"].remove(lista)
                                print("Removido")

                                with open("seleções.json", "w") as arq:
                                    json.dump(dados, arq, indent=4, ensure_ascii=False)
                                break

                            elif confirmacao == "N":
                                break
                            else:
                                print("Digite somente 'S' ou 'N' ")
                            continue
                break
        if encontrado == False:
            print("Não encontrado")

    elif escolha == 5:
        encontrado2 = False
        while  True:
            edit = input("Qual elemento? \n 1 - País \n 2 - Grupo \n 3 - Confederação \n 4 - Treinador \n Resposta: ")
            
            if numeros(edit):
                edit = int(edit)
                break

        while True:
            nome = (input("Fale o ID do País: "))
            if numeros(nome):
                nome = int(nome)
                break

        for l in dados["s"]: 
            if l["ID"] == nome:
                print("País encontrado")
                encontrado2 = True

            if encontrado2 == True:
                if edit == 1: 
                    novo_país = input("Digite o novo nome: ")
                    
                    if texto(novo_país):
                        l["País"] = novo_país
                        print("Edição feita com sucesso")
                        break
                        

                elif edit == 2:
                    novo_grupo = input("Digite o novo nome: ")
                    while True:
                        if novo_grupo == "":
                            print("Não pode digitar nada")
                        else:
                            break

                    l["Grupo"] = novo_grupo
                    break

                elif edit == 3:
                    novo_confederação = input("Digite o novo nome: ")

                    if texto(novo_confederação):
                        l["Confederação"] = novo_confederação
                        print("Edição feita com sucesso")
                        break

                elif edit == 4:
                    novo_treinador = input("Digite o novo nome: ")

                    if texto(novo_treinador):
                        l["Treinador"] = novo_treinador
                        print("Edição feita com sucesso")
                        break

        with open("seleções.json", "w") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)

        if encontrado2 == False:
            print("ID não encontrado")
            continue

    elif escolha == 6:
        print("Até a próxima!")
        break