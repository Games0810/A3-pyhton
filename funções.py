def texto(tex):
    if tex == "":
        print("Não pode digitar nada")
        return False
    
    elif not tex.replace(" ", "").isalpha():
        print("Digite somente letras")
        return False

    return True

def numeros(num):
    if num == "":
        print("Não pode deixar vazio")
        return False
        
    elif not num.replace(" ", "").isdigit():
        print("Digite somente números")
        return False
    
    return True