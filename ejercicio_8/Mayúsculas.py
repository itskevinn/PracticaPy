def inicio():
    mensaje = input("Ingrese el texto: ")
    charMssg = list(mensaje)
    mssg = []
    fmensaje = ""
    for char in charMssg:
        if(char >= 'a' and char <= 'z'):
            mssg += char
        else:
            mssg += ' '
            mssg += char
    for char in mssg:
        fmensaje += str(char)
    print(fmensaje.strip())
