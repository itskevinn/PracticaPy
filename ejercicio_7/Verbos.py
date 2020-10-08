
def conjVerbE(verb):
    print("Yo " + verb + "o")
    print("Tú " + verb + "es")
    print("Él " + verb + "e")
    print("Ella " + verb + "e")
    print("Nosotros " + verb + "emos")
    print("Ellos " + verb + "en")


def conjVerbI(verb):
    print("Yo " + verb + "o")
    print("Tú " + verb + "es")
    print("Él " + verb + "e")
    print("Ella " + verb + "e")
    print("Nosotros " + verb + "imos")
    print("Ellos " + verb + "en")


def conjVerbA(verb):
    print("Yo " + verb + "o")
    print("Tú " + verb + "as")
    print("Él " + verb + "a")
    print("Ella " + verb + "a")
    print("Nosotros " + verb + "amos")
    print("Ellos " + verb + "an")

def inicio():
    vConj = input("Ingrese el regular a conjugar: ")
    subStr = vConj[-2:]
    if(subStr == "er" or subStr == "ir" or subStr == "ar"):
        print("VERBO CONJUGADO")
        vAConj = vConj[:-2]
        if(subStr == "er"):
            conjVerbE(vAConj)
        elif (subStr == "ar"):
            conjVerbA(vAConj)
        elif(subStr == "ir"):
            conjVerbI(vAConj)
    else:
        print("No es verbo regular")
