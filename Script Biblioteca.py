import os
'''
Importamos el os para que le quede todo más limpio al usuario
'''
salida=False #Declaramos salida False y en el menú si el usuario quiere salir simplemente lo cambiaremos a True
print("")
print("¡Bienvenido a la biblioteca de SJO!")
pausa=input("Presiona Enter para continuar...")
#Declaramos los diccionarios de cada uno de los libros
libro1={"titulo":"Don Quijote de la Mancha", "autor":"Miguel de Cervantes", "disponibilidad":True, "resumen":"Una de las obras cumbres de la literatura universal, narra las aventuras de Alonso Quijano, un hidalgo obsesionado con los libros de caballería, quien decide convertirse en el caballero andante (Don Quijote). Junto a su fiel escudero, Sancho Panza, emprende disparatadas aventuras llenas de humor, crítica social y profundas reflexiones sobre la humanidad."}
libro2={"titulo":"La sombra del viento", "autor":"Carlos Ruiz Zafón", "disponibilidad":True, "resumen":"Un fascinante thriller literario ambientado en la Barcelona de la posguerra. Daniel Sempere descubre un libro titulado La sombra del viento, cuya misteriosa historia lo lleva a desentrañar secretos oscuros sobre su autor y a vivir una trama de amor, pasión y traición."}
libro3={"titulo":"Los renglones torcidos de Dios", "autor":"Torcuato Luca de Tena", "disponibilidad":True, "resumen":"Alice Gould, una investigadora privada, se interna voluntariamente en un hospital psiquiátrico para resolver un caso, pero pronto su cordura es puesta en duda. Este apasionante relato cuestiona los límites entre la locura y la realidad, atrapando al lector en un torbellino psicológico."}
libro4={"titulo":"El tiempo entre costuras", "autor":"María Dueñas", "disponibilidad":True, "resumen":"Sira Quiroga, una joven costurera madrileña, ve su vida cambiar radicalmente cuando se traslada a Marruecos. Entre intrigas políticas, espionaje y supervivencia, Sira construye un futuro en una novela que mezcla romance, drama histórico y superación personal."}
libro5={"titulo":"Cien años de soledad", "autor":"Gabriel García Márquez", "disponibilidad":True, "resumen":"Una obra maestra del realismo mágico que cuenta la historia de la familia Buendía en el mítico pueblo de Macondo. Con personajes inolvidables y una narrativa exuberante, aborda temas como el amor, la soledad, el tiempo y el destino en un ciclo interminable de generaciones."}
#Y declaramos un diccionario general
libros={1:libro1, 2:libro2, 3:libro3, 4:libro4, 5:libro5}
salir_reserva=False
def ver_catalogo():
    print(" ")
    '''
    Usamos el for para que recorra el diccionario general posición por posición,
    llamando tanto ["titulo"] tanto como ["autor"] de cada libro.
    '''
    for i in libros:
        print(i,libros[i]["titulo"]," - ",libros[i]["autor"])
        print("*********************************************************")
    print(" ")
    input("Presiona Enter para continuar...")

def consultar_disponibilidad(libro_entrada):
    '''
    Aquí simplemente llamamos al libro que ha introducido el usuario y verificamos si la disponibilidad es "True" o "False",
    también gestionamos el error de que el usuario ponga un título diferente a los que hay en la biblioteca.
    '''
    encontrado = False  # Nos servirá para saber si lo hemos encontrado o no
    for i in libros:  
        if libros[i]["titulo"] == libro_entrada:  # Comparamos el título ingresado con los títulos en el diccionario
            encontrado = True
            if libros[i]["disponibilidad"] == True: #Verificamos su disponibilidad
                print("Está disponible")
            else:
                print("El libro no está disponible en estos momentos")        
    if encontrado==False: #Si no encuentra el libro encontrado se mantendrá False y dará este mensaje
        print("Has introducido un título inexistente en nuestra biblioteca")
    input("Presiona Enter para continuar...")

def reservar_libro(libro_entrada):
    '''
    Hacemos que el usuario introduzca el título del libro que quiera reservar. Verificamos que está disponible,
    si no, enviamos un mensaje diciéndole que no está disponible. Si está disponible, le enviamos un mensaje de confirmación
    '''
    
    for i in libros:  
        if libros[i]["titulo"] == libro_entrada:  # Comparamos 
            
            if libros[i]["disponibilidad"]==True:  # Verificamos si está disponible
                    libros[i]["disponibilidad"] = False  # Actualizamos la disponibilidad
                    print(f"Reservado con éxito el libro: {libros[i]['titulo']}")
                    salir_reserva = True
                    input("Presiona Enter para continuar...")
            else:
                print("El libro no se puede reservar en estos momentos")
                input("Presiona Enter para continuar...")
    return salir_reserva        
    

def devolver_libro(entrada):
    '''
    Permite al usuario devolver un libro previamente reservado. Si el libro está reservado, se devuelve y su disponibilidad
    se actualiza. Si no está reservado o el título no existe, se muestra el mensaje correspondiente.
    '''
    
    encontrado = False  # Para indicar si ha encontrado o no

    for i in libros:  
        if libros[i]["titulo"] == entrada:  # Comparamos 
            encontrado = True
            if libros[i]["disponibilidad"]==False:  # Verificamos si el libro está reservado
                libros[i]["disponibilidad"] = True  # Actualizamos la disponibilidad
                print(f"Devuelto con éxito el libro: {libros[i]['titulo']}")
                pausa = input("Presiona Enter para continuar...")
            else:
                print("El libro no se puede devolver porque no está reservado.")
                input("Presiona Enter para continuar...")
    if encontrado==False:
        print("Has introducido un título inexistente en nuestra biblioteca.")
        input("Presiona Enter para continuar...")

def ver_resumen(titulo_entrada):
    encontrado_resumen = False #Nos servirá como referencia para saber si el bucle ha encontrado el titulo puesto por el usuario o no
    for i in libros:
        if libros[i]["titulo"] == titulo_entrada:#Iniciado el bucle en el diccionario general de libros y comparando con el titulo de entrada puesto por el usuario
            encontrado_resumen=True #Aquí ya lo encontraría y pasaría a mostrar el resumen de dicho libro
            print("**************************************************************************************************************************************************************")
            print(libros[i]["resumen"])
            print("**************************************************************************************************************************************************************")
            input("Presiona Enter para continuar...")
    if  encontrado_resumen == False: #En caso de que no se haya encontrado el título introducido por el usuario se mantendría en False y les mostrariamos un mensaje al usuario de error por pantalla
        print("Has introducido un título inexistente")
        input("Presiona Enter para continuar...")

def limpiar_pantalla():
    '''
    he aprendido a usar la librería importada de os, y depende si es windows,
    se ejecuta de una manera diferente que si es linux o macOS.
    '''
    if os.name == 'nt':  # Si es Windows 
        os.system('cls')
    else:  # Si es macOS o Linux
        os.system('clear')
    '''
    Esto lo he hecho porque se que Paco su sistema operativo es macOS y creo que el de Carlos es windows
    Depende quien corrija se le activará una función o otra.
    '''
while salida==False:
    #Llamo a limpiar pantalla 
    limpiar_pantalla()
    print("")
    print("¿Qué desea hacer?")
    print("")
    print("(V): Ver catálogo de libros")
    print("(A): Ver resumen de un libro")
    print("(C): Consultar disponibilidad de un libro")
    print("(R): Reservar un libro")
    print("(D): Devolver libro")
    print("(S): Salir de la aplicación")
    print("")

    eleccion=input("").upper()
    
    match eleccion:
        case "V":
            ver_catalogo()
        
        case "A":
            print(" ")
            resumen=input("Introduce el título del libro: ")
            print(" ")
            ver_resumen(resumen)

        case "C":
            print(" ")
            print("Introduce el título del libro que quieras consultar su disponibilidad:")
            print(" ")
            libro_disponibilidad = input("")
            consultar_disponibilidad(libro_disponibilidad)

        case "R":
            
            while salir_reserva==False:
                print("")
                print("Introduce el título del libro que quieras reservar")
                print("") 
                eleccion_reserva = input("Título del libro: ")
                print(" ")
                reservar_libro(eleccion_reserva)
                
                if salir_reserva==False:
                    print("Has introducido un título inexistente en nuestra biblioteca")
                    input("Presiona Enter para continuar...")

        case "S":
            salida=True
            print("Gracias por usar la biblioteca de SJO")
        
        case "D":
            print("")
            print("Introduce el título del libro que quieras devolver:")
            print("")
            libro_devuelto = input("Título del libro: ")
            print("")
            devolver_libro(libro_devuelto)   
        
        case _:
            print("Introduce un carácter válido")
            input("Presiona Enter para continuar...")