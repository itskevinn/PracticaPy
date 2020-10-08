def inicio():
    Resultados()

def compararElementos(elementos):
    i = 0
    contador = 0
    elementoSig = ""
    for i in range(4):
        if i < 3:
            elementoSig = elementos[i + 1]
            if elementos[i] == elementoSig:
                contador = contador + 1
                if(contador == 3):
                    return True
    return False

def Resultados():
    i = 0
    elementos = []
    print("RESULTADO MÁQUINA TRAGAMONEDAS")
    print("Ingrese los 4 dígitos del resultado")
    for i in range(4):
        elementos.append(input("Ingrese el resultado número " + str(i) + ": "))
        i = i+1
    if compararElementos(elementos):
        print("¡¡¡JACK POT!!!")
    else:
        print("NO MERECE PREMIO!")