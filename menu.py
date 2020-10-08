from ejercicio_1 import Ejercicio_Nemo
from ejercicio_2 import Segundo_Ejercicio
from ejercicio_3 import Tercer_Ejercicio
from ejercicio_4 import inicio
from ejercicio_5 import Fechas
from ejercicio_6 import NumerosPandigitales
from ejercicio_7 import Verbos
from ejercicio_8 import Mayúsculas
from ejercicio_9 import Personas


def cls(): print("\n" * 100)


opcion = 0
while opcion < 10:
    cls()
    print("      ------------------------------------")
    print("      -Menu Principal-")
    print("      -1. Ejercicio 1            -")
    print("      -2. Ejercicio 2            -")
    print("      -3. Ejercicio 3            -")
    print("      -4. Ejercicio 4            -")
    print("      -5. Ejercicio 5            -")
    print("      -6. Ejercicio 6            -")
    print("      -7. Ejercicio 7            -")
    print("      -8. Ejercicio 8            -")
    print("      -9. Ejercicio 9            -")
    print("      -10. Salir            -")
    print("      ------------------------------------")
    opcion = int(input("Ingresa una opcion: "))

    if(opcion == 1):
        cls()
        Ejercicio_Nemo.Nemo()
    elif(opcion == 2):
        cls()
        Segundo_Ejercicio.inicio()
    elif(opcion == 3):
        cls()
        Tercer_Ejercicio.inicio()
    elif(opcion == 4):
        cls()
        inicio.inicio()
    elif(opcion == 5):
        cls()
        Fechas.Fecha()
    elif(opcion == 6):
        cls()
        NumerosPandigitales.NumerosPandigitales()
    elif(opcion == 7):
        cls()
        Verbos.inicio()
    elif(opcion == 8):
        cls()
        Mayúsculas.inicio()
    elif(opcion == 9):
        cls()
        Personas.inicio()
