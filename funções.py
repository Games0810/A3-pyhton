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

        if texto(msg):
            break

    return msg

def validar_numero(numero):
    while True:
        ID_lista = input(numero).strip()

        if numeros(ID_lista):
            break
        
    ID_lista = int(ID_lista)
    return ID_lista
    


