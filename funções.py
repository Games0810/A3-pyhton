def texto(tex):
    #Verifica se o texto digatado é vazio
    if tex == "":
        print("Não pode digitar nada")
        return False
    
    #Verifica se o texto digitado só tem letras
    elif not tex.replace(" ", "").isalpha():
        print("Digite somente letras")
        return False

    #Se tudo certo, retorna verdadeiro
    return True

def numeros(num):
    #Verifica se o texto digatado é vazio
    if num == "":
        print("Não pode deixar vazio")
        return False
    
    #Verifica se o texto digatado só tem números
    elif not num.replace(" ", "").isnumeric():
        print("Digite somente números")
        return False
    
    #Se tudo certo, retorna verdadeiro
    return True

def validar_texto(mensagem):
    while True:
        msg = input(mensagem).strip()

        #Faz a validação da variável "msg" dentro do loop até o valor ser válido
        if texto(msg):
            break

    return msg

def validar_numero(numero):
    while True:
        num_lista = input(numero).strip()

        #Faz a validação da variável "ID_lista" dentro do loop até o valor ser válido 
        if numeros(num_lista):
            break
    
    #Converte a váriavel em "int" para encontrar os IDs do arquivo .json
    num_lista = int(num_lista)
    return num_lista
    


