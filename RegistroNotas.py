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


