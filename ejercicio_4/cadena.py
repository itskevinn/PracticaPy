def crear_cadena(lista):
  i = 0
  cadena = ""
  while len(lista) > i:
    cadena = cadena + lista[i]
    i += 1 
  return cadena