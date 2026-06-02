import json
from random import randint
from funções import texto
from funções import numeros 
from funções import validar_texto
from funções import validar_numero



while True:
    #Abre o arquivo .json e carrega os itens dentro da variável "dados"
    with open("seleções.json", "r", encoding="utf-8") as arq:
        dados = json.load(arq)
    permissao1 = False
    #Tabela de opções
    print("""
Bem vindo, escolha uma das coisas a seguir:
1- Ver lista
2- Ver o cadastro de um país
3- Adicionar
4- Excluir
5- Editar
6- Sair""")
    
    escolha = input("Resposta: ").strip()

    #Função é chamada dentro do "if"
    if numeros(escolha):
        escolha = int(escolha)
        permissao1 = True
    
    #Condição para caso a pessoa digite um número que não seja dentro lista 
    if escolha not in (1,2,3,4,5,6) and permissao1 == True:
        print("Escolha um número na lista")

    if escolha == 1:
        #Percorre a lista 
        for lista in dados["s"]:
            #Todos os itens são mostrados
            print("-="*20)
            print(f"ID: {lista['ID']}")
            print(f"País: {lista['País']}")
            print(f"Grupo: {lista['Grupo']}")
            print(f"Confederação: {lista['Confederação']}")
            print(f"Treinador: {lista['Treinador']}")
            print("-="*20)

    elif escolha == 2:
        while True:
            encontrado3 = False
            lista_nome = validar_numero("Fale o ID do país: ")

            #Função é chamada dentro do "if"
            if numeros(lista_nome):
                lista_nome = int(lista_nome)
                break

        #Percorre a lista 
        for pais in dados["s"]:
            print("-="*20)
            if pais["ID"] == lista_nome:
                    encontrado3 = True
                    #Os itens do país pedido são mostrados
                    print(f"ID: {pais['ID']}")
                    print(f"País: {pais['País']}")
                    print(f"Grupo: {pais['Grupo']}")
                    print(f"Confederação: {pais['Confederação']}")
                    print(f"Treinador: {pais['Treinador']}")
                    print("-="*20)

        #Caso o país não seja encontrado
        if encontrado3 == False:
            print("País não encontrado")


    elif escolha == 3:
        #Sistema de criação de ID
        while True:
            duplicado = False
            novo_id = ""
            id = ""
            for num in range (10):
                num = randint(1,9)
                id += str(num)
            id = int(id)
            for ids in dados["s"]:
                if id == ids["ID"]:
                    duplicado = True
            
            #Caso tenha um ID duplicado, o sistema reinicia
            if duplicado == True:
                continue
            
            #Caso não tenha um ID duplicado, o ID é criado
            elif duplicado == False:
                novo_id = id
                break
 

        novo_p = validar_texto("País: ")
        novo_g = validar_texto("Grupo: ")
        novo_c = validar_texto("Confederação: ")
        novo_t = validar_texto("Treinador: ")

        #Os itens são adicionados dentro de uma biblioteca 
        nova_seleção = {"País": novo_p, "Grupo": novo_g, "Confederação": novo_c, "Treinador": novo_t, "ID": novo_id}
        #A biblioteca é adicionada dentro da váriavel "dados"
        dados["s"].append(nova_seleção)

        #As alterações são escritas no arquivo .json
        with open("seleções.json", "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)

    elif escolha == 4:
        encontrado = False
        while True:
            remover = input("Fale o ID do país: ").strip()

            if numeros(remover):
                remover = int(remover)
                break 

        #Percorre a lista 
        for lista in dados["s"]:
            if lista["ID"] == remover:
                print("ID encontrado")
                encontrado = True
                if encontrado == True:
                        while True: 
                            confirmacao = input(f"Você realmente desejar excluir os dados do país {lista["País"]}? [S/N]").upper().strip()
                            
                            if confirmacao == "S":
                                #Remove o item dentro da váriavel "dados"
                                dados["s"].remove(lista)
                                print("Removido")

                                #As alterações são escritas no arquivo .json
                                with open("seleções.json", "w", encoding="utf-8") as arq:
                                    json.dump(dados, arq, indent=4, ensure_ascii=False)
                                break

                            elif confirmacao == "N":
                                break
                            #Caso digite algo diferente
                            else:
                                print("Digite somente 'S' ou 'N' ")
                            continue

        #Caso o país não seja encontrado
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
            
            #Caso o valor digitado seja um número e que está 
            if pode1 == True and pode2 == True:
                break

        while True:
            nome = (input("Fale o ID do País: ")).strip()
            if numeros(nome):
                nome = int(nome)
                break

        #Percorre a lista
        for l in dados["s"]: 
            if l["ID"] == nome:
                print("País encontrado")
                encontrado2 = True

            if encontrado2 == True:
                if edit == 1:
                    while True:
                        novo_país = input("Digite o novo nome: ").strip()
                        
                        if texto(novo_país):
                            #Troca o item antigo pelo novo item
                            l["País"] = novo_país
                            print("Edição feita com sucesso")
                            #Quebra o laço de repetição "while"
                            break

                elif edit == 2:
                    while True:
                        novo_grupo = input("Digite o novo nome: ").strip()
                        if texto(novo_grupo):
                            l["Grupo"] = novo_grupo
                            print("Edição feita com sucesso")
                            break

                elif edit == 3:
                    while True:
                        novo_confederação = input("Digite o novo nome: ").strip()
                        if texto(novo_confederação):
                            l["Confederação"] = novo_confederação
                            print("Edição feita com sucesso")
                            break

                elif edit == 4:
                    while True:
                        novo_treinador = input("Digite o novo nome: ").strip()
                        if texto(novo_treinador):
                            l["Treinador"] = novo_treinador
                            print("Edição feita com sucesso")
                            break

                #Quebra o laço de repetição "for"
                break

        #As alterações são escritas no arquivo .json
        with open("seleções.json", "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)
        
        #Caso o país não seja encontrado
        if encontrado2 == False:
            print("ID não encontrado")
            continue

    elif escolha == 6:
        #O programa se encerra
        print("Até a próxima!")
        break