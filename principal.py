import json
from random import randint


while True:
    print("""
Bem vindo, escolha uma das coisas a seguir:
1- Ver lista
2- Ver o cadastro de um país
3- Adicionar
4- Excluir
5- Editar
6- Sair""")
    try:
        escolha=int(input(" Resposta: "))

    except ValueError:
        print("Digite um número")
        continue

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
        lista_nome = str(input("Digite o nome do país: "))
        if lista_nome == "":
            print("Não pode digitar nada")
        elif not lista_nome.replace(" ", "").isalpha():
            print("Digite somente letras")
        else: 
            for p in dados["s"]:
                if p["País"] == lista_nome:
                    print("-="*20)
                    print(f"ID: {p['ID']}")
                    print(f"País: {p['País']}")
                    print(f"Grupo: {p['Grupo']}")
                    print(f"Confederação: {p['Confederação']}")
                    print(f"Treinador: {p['Treinador']}")
                    print("-="*20)
            else: 
                print("País não encontrado")


    elif escolha == 3:
        id_criado = False
        duplicado = False
        while True:
            novo_id = ""
            id = ""
            for i in range (10):
                n = randint(0, 9)
                id += str(n)
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
            novo_p = input("País: ").strip()

            if novo_p == "":
                print("Não pode digitar nada")
                continue
            elif not novo_p.replace(" ", "").isalpha():
                print("Digite somente letras")
                continue
            else:
                break 
        
        while True:
            novo_g = input("Grupo: ").strip()

            if novo_g == "":
                print("Não pode digitar nada")
                continue
            else:
                break

        while True:
            novo_c = input("Confederação: ").strip()

            if novo_c == "":
                print("Não pode digitar nada")
                continue
            elif not novo_c.replace(" ", "").isalpha():
                print("Digite somente letras")
                continue
            else: 
                break

        while True:
            novo_t = input("Treinador: ").strip()

            if novo_t == "":
                print("Não pode digitar nada")
                continue
            elif not novo_t.replace(" ", "").isalpha():
                print("Digite somente letras")
                continue
            else: 
                break

        nova_seleção = {"País": novo_p, "Grupo": novo_g, "Confederação": novo_c, "Treinador": novo_t, "ID": int(novo_id)}
        dados["s"].append(nova_seleção)

        with open("seleções.json", "w") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
    
    elif escolha == 4:
        try:
            remover = int(input("Fale o ID do país: "))

        except ValueError:
            print("Digite somente números")
            continue

        for lista in dados["s"]:
            if lista["ID"] == remover:
                dados["s"].remove(lista)
                print("Removido")
                break      
        else:
            print("Não encontrado")

        with open("seleções.json", "w") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)

    elif escolha == 5:
        edit = int(input("Qual elemento? \n 1 - País \n 2 - Grupo \n 3 - Confederação \n 4 - Treinador "))
        if edit == 1:
            nome = int(input("Fale o ID do País: "))
            for l in dados["s"]: 
                if l["ID"] == nome:
                    novo_país = str(input("Digite o novo nome: "))

                    if novo_país == "":
                        print("Não pode digitar nada")
                    elif not novo_país.replace(" ", "").isalpha():
                        print("Digite somente letras")

                    l["País"] = novo_país
            with open("seleções.json", "w") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)

        elif edit == 2:
            nome = input("Fale o ID do País: ")
            for l in dados["s"]: 
                if l["ID"] == nome:
                    novo_grupo = input("Digite o novo nome: ")

                    if novo_grupo == "":
                        print("Não pode digitar nada")
                    elif not novo_grupo.replace(" ", "").isalpha():
                        print("Digite somente letras")

                    l["Grupo"] = novo_grupo
            with open("seleções.json", "w") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)

        elif edit == 3:
            nome = input("Fale o ID do País: ")
            for l in dados["s"]: 
                if l["ID"] == nome:
                    novo_confederação = input("Digite o novo nome: ")
                    l["Confederação"] = novo_confederação
            with open("seleções.json", "w") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)

        elif edit == 4:
            nome = input("Fale o ID do País: ")
            for l in dados["s"]: 
                if l["ID"] == nome:
                    novo_treinador = input("Digite o novo nome: ")
                    l["Treinador"] = novo_treinador
            with open("seleções.json", "w") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)

    elif escolha == 6:
        break