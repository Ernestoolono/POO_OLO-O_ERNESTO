# Diccionario vacío para almacenar la información
estudiantes = {}

# Menú Principal
while True:
    print("\nMenú opciones:")
    print("1. Agregar estudiante:")
    print("2. Consultar calificaciones:")
    print("3. Mostrar estudiantes")
    print("4. Salir")

    opcion = input("Ingrese la opcion deseada: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        calificaciones = {}
        while True:
            materia = input("Ingrese el nombre de la materia (o 'salir' para terminar): ")
            if materia.lower() == "salir":
                break
            try:
                calificacion = float(input(f"Ingrese la calificación de {materia}: "))
            except ValueError:
                print("La calificación debe ser un número decimal. Intente nuevamente.")
            else:
                calificaciones[materia] = calificacion
        estudiantes[nombre] = calificaciones
        print(f"Estudiante {nombre} agregado correctamente.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del estudiante: ")
        if nombre in estudiantes:
            calificaciones = estudiantes[nombre]
            print(f"Calificaciones de {nombre}:")
            for materia, calificacion in calificaciones.items():
                print(f"{materia}: {calificacion:.2f}")  # Format with two decimals
        else:
            print(f"El estudiante {nombre} no está registrado.")
    elif opcion == "3":
        if estudiantes:
            print("Lista de estudiantes:")
            for nombre, calificaciones in estudiantes.items():
                print(f"{nombre}: {calificaciones}")
        else:
            print("No hay estudiantes registrados.")
    elif opcion == "4":
        print(f"¡Gracias por usar el programa.")
        exit()
    else:
        print("Opción no válida. Intente nuevamente.")
