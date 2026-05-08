def texto(tex):
    if tex == "":
        print("Nâo pode digitar nada")
        return False
    elif not tex.replace(" ", "").isalpha():
        print("Digite somente letras")
        return False
    return True

def numeros(num):
    if num == "":
        print("Nâo pode digitar nada")
        return False
    elif not num.replace(" ", "").isnumeric():
        print("Digite somente números")
        return False
    return True