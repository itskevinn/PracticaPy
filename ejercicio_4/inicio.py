def inicio():
  i=0
  lista = []
  cantidad = int(input("digite tamaño de la lista: "))
  print("\n-------------")
  while cantidad > i:
    temp = input("digite dato: ")
    lista.append(temp)
    i += 1
  print("-------------\n")
  
  print("Entrada: ",lista)
  print("Salida: ",cadena.crear_cadena(lista))
