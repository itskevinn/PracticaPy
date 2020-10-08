def inicio():
    print("Ingrese una cadena con mayucuslas y minusculas")
    Imprimir()

def Mayuscula(letra):   
    letras=list(letra)
    parte1 = ""
    parte2=""
    for i in letras:
        if i >= 'A' and i <= 'Z':
            parte1+=i
        else:
            parte2+=i
    resultado=parte1+parte2
    return resultado

def Imprimir():
    letra=input("Ingrese los datos: ")

    print(Mayuscula(letra))