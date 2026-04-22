import json
from random import randint


while True:
    try:
        escolha = int(input("""
    Bem vindo, escolha uma das coisas a seguir:
    1 - Ver lista
    2- Adicionar
    3- Excluir
    4- Editar
    5- Sair
        Resposta: """))
    
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
            novo_id = ""
            for i in range (10):
                n = randint(1, 10)
                novo_id += str(n)
            novo_p = input("País: ")
            novo_g = input("Grupo: ")
            novo_c = input("Confederação: ")
            novo_t = input("Treinador: ")
    
            nova_seleção = {"País": novo_p, "Grupo": novo_g, "Confederação": novo_c, "Treinador": novo_t, "ID": novo_id}
            dados["s"].append(nova_seleção)
    
            with open("seleções.json", "w") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)
        
        elif escolha == 3:
            remover = input("Nome do País: ")
            for lista in dados["s"]:
                if lista["País"] == remover:
                    dados["s"].remove(lista)
                    print("Removido")
                    break
            
                else:
                    print("Não encontrado")
    
            with open("seleções.json", "w") as arq:
                json.dump(dados, arq, indent=4, ensure_ascii=False)
    
        elif escolha == 4:
            edit = int(input("Qual elemento? \n 1- País \n 2 - Grupo \n 3 - Confederação \n "))
            if edit == 1:
                nome = input("Fale o nome do País: ")
                for l in dados["s"]: 
                    if l["País"] == nome:
                        novo_país = input("Digite o novo nome: ")
                        l["País"] = novo_país
                with open("seleções.json", "w") as arq:
                    json.dump(dados, arq, indent=4, ensure_ascii=False)
    
            elif edit == 2:
                nome = input("Fale o nome do País: ")
                for l in dados["s"]: 
                    if l["País"] == nome:
                        novo_grupo = input("Digite o novo nome: ")
                        l["Grupo"] = novo_grupo
                with open("seleções.json", "w") as arq:
                    json.dump(dados, arq, indent=4, ensure_ascii=False)
            elif edit == 3:
                nome = input("Fale o nome do País: ")
                for l in dados["s"]: 
                    if l["País"] == nome:
                        novo_confederação = input("Digite o novo nome: ")
                        l["Confederação"] = novo_confederação
                with open("seleções.json", "w") as arq:
                    json.dump(dados, arq, indent=4, ensure_ascii=False)
    
        elif escolha == 5:
            break
    except ValueError:
        print("- CAIXAS VAZIAS NÃO SÃO ACEITAS -")
