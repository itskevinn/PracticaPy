def Nemo():
    lista = []
    cadena = input("ingrese la cadena: ")
    lista = cadena.split(' ')
    encontro = False
    cont = 1
    for i in lista:
        if(i=="Nemo"):
            print("Se encontró la palabra Nemo en la posición", cont)
            encontro = True
        else:
            cont=cont+1
            

    if(encontro==False):
        print("No se encontro la palabra Nemo en la cadena")