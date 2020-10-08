def inicio():
    opcion = 0

    personas = []
    id = 1

    while opcion < 5:
        print("      ------------------------------------")
        print("      -Que acción deseas realizar        -")
        print("      -1. Agregar nuevo usuario          -")
        print("      -2. Editar un usuario              -")
        print("      -3. Eliminar un usuario            -")
        print("      -4. Listar todos todos los usuarios-")
        print("      -5. Salir                          -")
        print("      ------------------------------------")
        opcion = int(input("Ingresa una opción: "))

        if(opcion == 1):
            nombres = input("Ingresa los nombres del usuario: ")
            apellidos = input("Ingresa los apellidos del usuario: ")
            celular = input("Ingresa el celular del usuario: ")

            personas.append({
                "id": id,
                "nombres": nombres,
                "apellidos": apellidos,
                "celular": celular
            })
            id += 1
            print("El usuario", nombres, "se ha agregado correctamente")
        elif(opcion == 2):
            usuario_eliminar = int(input("Ingrese el id del usuario a editar: "))
            index_eliminar = -1
            usuario = {}
            for index, persona in enumerate(personas):
                if(usuario_eliminar == persona["id"]):
                    index_eliminar = index
                    usuario = persona

            if(index_eliminar == -1):
                print("No se ha encontrado ningun usuario con el id", usuario_eliminar)
            else:
                print("Actualizando datos del usuario", usuario['nombres'],", dejar los campos en blanco si no desea cambiar la información")
                nombres = input("Nombres (" + usuario['nombres'] + "): ")
                apellidos = input("Apellidos (" + usuario['apellidos'] + "): ")
                celular = input("Celular (" + usuario['celular'] + "): ")

                if(nombres != ""):
                    usuario['nombres'] = nombres
                
                if(apellidos != ""):
                    usuario['apellidos'] = apellidos

                if(celular != ""):
                    usuario['celular'] = celular

                personas[index_eliminar] = usuario
                print("El usuario", usuario['nombres'], "ha sido actualizado correctamente")

        elif(opcion == 3):
            usuario_eliminar = int(input("Ingrese el id del usuario a eliminar: "))
            index_eliminar = -1
            usuario = {}
            for index, persona in enumerate(personas):
                if(usuario_eliminar == persona["id"]):
                    index_eliminar = index
                    usuario = persona

            if(index_eliminar == -1):
                print("No se ha encontrado ningun usuario con el id", usuario_eliminar)
            else:
                del personas[index_eliminar]
                print("El usuario", usuario['nombres'], "se ha eliminado correctamente")
        elif(opcion == 4):
            if(not len(personas)):
                print("No se han encontrado registros")
            else:
                print("Listado de usuarios")
                print("__________")
                print("ID|Nombres|Apellidos|Celular")
                for persona in personas:
                    print(persona["id"],"|",persona["nombres"],"|",persona["apellidos"],"|",persona["celular"])
                print("__________")
        
        if(opcion != 5):
            input("Presione cualquier tecla para continuar...")

    print("Gracias por utilizar el programa")