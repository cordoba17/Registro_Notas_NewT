print("Selecciona la opción que te corresponda:")
select = input("a) Estudiante\nb) Profesor\n> ")

match select:
    case "a":
        print("\nBienvenido Estudiante")
    case "b":
        print("\nBienvenido Profesor")
    case _:
        print("\nOpción no válida. Saliendo del programa.")
        exit()

# Registro de usuario
print("\nPor favor, registra el correo y la contraseña:")
userCorrectly = input("Digite el correo que desea registrar: ")
passwordCorrectly = input("Digite la contraseña que desea registrar: ")

# Inicio de sesión
print("\nInicia sesión")
user = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

if user == userCorrectly and password == passwordCorrectly:
    print(f"\nBienvenido {user} ✅")

     # Menú de materias
    while True:
        print("\n📚 MENÚ DE MATERIAS")
        print("1. Matemáticas")
        print("2. Inglés")
        print("3. Química")
        print("4. Salir")

        opcion = input("Selecciona una materia (1-4): ")

        match opcion:
            case "1":
                print("\n📘 Has seleccionado Matemáticas.")
            case "2":
                print("\n📗 Has seleccionado Inglés.")
            case "3":
                print("\n📙 Has seleccionado Química.")
            case "4":
                print("\n👋 Saliendo del programa. ¡Hasta luego!")
                break
            case _:
                print("\n❌ Opción no válida. Intenta de nuevo.")
else:
    print("\n❌ Error: Correo o contraseña incorrectos.")
