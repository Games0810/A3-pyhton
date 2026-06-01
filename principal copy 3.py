import json
from random import randint
from funções import texto
from funções import numeros 



while True:
    with open("seleções.json", "r", encoding="utf-8") as arq:
        dados = json.load(arq)
    permissao1 = False
    print("""
Bem vindo, escolha uma das coisas a seguir:
1- Ver lista
2- Ver o cadastro de um país
3- Adicionar
4- Excluir
5- Editar
6- Sair""")
    escolha = input("Resposta: ").strip()

    if numeros(escolha):
        escolha = int(escolha)
        permissao1 = True

    if escolha not in (1,2,3,4,5,6) and permissao1 == True:
        print("Escolha um número na lista")

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
            lista_nome = input("Fale o ID do país: ").strip()

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
        while True:
            duplicado = False
            novo_id = ""
            id = ""
            for i in range (10):
                n = randint(1,9)
                id += str(n)
            id = int(id)
            for ids in dados["s"]:
                if id == ids["ID"]:
                    duplicado = True
            
            if duplicado == True:
                continue

            if duplicado == False:
                novo_id = id
                break
 

        while True:
            novo_p = input("País: ").strip()

            if texto(novo_p):
                break
        
        while True:
            novo_g = input("Grupo: ").strip()

            if texto(novo_g):
                break

        while True:
            novo_c = input("Confederação: ").strip()

            if texto(novo_c):
                break

        while True:
            novo_t = input("Treinador: ").strip()

            if texto(novo_t):
                break

        nova_seleção = {"País": novo_p, "Grupo": novo_g, "Confederação": novo_c, "Treinador": novo_t, "ID": novo_id}
        dados["s"].append(nova_seleção)

        with open("seleções.json", "w", encoding="utf-8") as arq:
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

                                with open("seleções.json", "w", encoding="utf-8") as arq:
                                    json.dump(dados, arq, indent=4, ensure_ascii=False)
                                break

                            elif confirmacao == "N":
                                break
                            else:
                                print("Digite somente 'S' ou 'N' ")
                            continue
        if encontrado == False:
            print("Não encontrado")

    elif escolha == 5:
        encontrado2 = False
        pode2 = False
        while  True:
            pode1 = False
            edit = input("Qual elemento? \n 1 - País \n 2 - Grupo \n 3 - Confederação \n 4 - Treinador \n Resposta: ").strip()

            if numeros(edit):
                edit = int(edit)
                pode1 = True
            
            if pode1 == True:    
                if edit not in (1,2,3,4):
                    print('Digite um número da lista')
                else:
                    pode2 = True

            if pode1 == True and pode2 == True:
                break

        while True:
            nome = (input("Fale o ID do País: ")).strip()
            if numeros(nome):
                nome = int(nome)
                break

        for l in dados["s"]: 
            if l["ID"] == nome:
                print("País encontrado")
                encontrado2 = True

            if encontrado2 == True:
                if edit == 1:
                    while True:
                        novo_país = input("Digite o novo nome: ").strip()
                        
                        if texto(novo_país):
                            l["País"] = novo_país
                            print("Edição feita com sucesso")
                            break
                    break
                        

                elif edit == 2:
                    novo_grupo = input("Digite o novo nome: ").strip()
                    if texto(novo_grupo):
                        l["Grupo"] = novo_grupo
                        print("Edição feita com sucesso")
                        break

                elif edit == 3:
                    novo_confederação = input("Digite o novo nome: ").strip()

                    if texto(novo_confederação):
                        l["Confederação"] = novo_confederação
                        print("Edição feita com sucesso")
                        break

                elif edit == 4:
                    novo_treinador = input("Digite o novo nome: ").strip()

                    if texto(novo_treinador):
                        l["Treinador"] = novo_treinador
                        print("Edição feita com sucesso")
                        break

        with open("seleções.json", "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
        
        if encontrado2 == False:
            print("ID não encontrado")
            continue

    elif escolha == 6:
        print("Até a próxima!")
        break