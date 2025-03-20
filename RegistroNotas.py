import json
import os

# Archivo donde se guardarán las notas
archivo_notas = "notas.json"

# 📌 Cargar las notas desde el archivo si existe, o inicializar un diccionario vacío
if os.path.exists(archivo_notas):
    with open(archivo_notas, "r") as file:
        notas = json.load(file)
else:
    notas = {
        "Matemáticas": {},
        "Inglés": {},
        "Química": {}
    }

# Selección de usuario
print("Selecciona la opción que te corresponda:")
select = input("a) Estudiante\nb) Profesor\n> ").strip().lower()

match select:
    case "a":
        print("\nBienvenido Estudiante")
        rol = "estudiante"
    case "b":
        print("\nBienvenido Profesor")
        rol = "profesor"
    case _:
        print("\n❌ Opción no válida. Saliendo del programa.") 
        exit()

# Registro de usuario
print("\nPor favor, registra el correo y la contraseña:")
userCorrectly = input("Digite el correo que desea registrar: ").strip()
passwordCorrectly = input("Digite la contraseña que desea registrar: ").strip()

# Inicio de sesión
print("\nInicia sesión")
user = input("Ingrese usuario: ").strip()
password = input("Ingrese contraseña: ").strip()

if user == userCorrectly and password == passwordCorrectly:
    print(f"\n✅ Bienvenido {user}")

    while True:
        print("\n📚 MENÚ DE MATERIAS")
        print("1. Matemáticas")
        print("2. Inglés")
        print("3. Química")
        print("4. Salir")

        opcion = input("Selecciona una materia (1-4): ").strip()

        match opcion:
            case "1":
                materia = "Matemáticas"
            case "2":
                materia = "Inglés"
            case "3":
                materia = "Química"
            case "4":
                print("\n👋 Saliendo del programa. ¡Hasta luego!")
                
                # 📌 Guardar las notas en el archivo antes de salir
                with open(archivo_notas, "w") as file:
                    json.dump(notas, file, indent=4)

                break
            case _:
                print("\n❌ Opción no válida. Intenta de nuevo.")
                continue

        if rol == "profesor":
            estudiante = input("\nIngrese el nombre del estudiante: ").strip()
            nota = input(f"Ingrese la nota de {estudiante} en {materia}: ").strip()

            # 📌 Si el estudiante no tiene notas en la materia, inicializamos una lista
            if estudiante not in notas[materia]:
                notas[materia][estudiante] = []

            # Agregar la nueva nota a la lista
            notas[materia][estudiante].append(nota)

            # 📌 Guardar automáticamente cada vez que se agregan notas
            with open(archivo_notas, "w") as file:
                json.dump(notas, file, indent=4)

            print(f"\n✅ Nota registrada: {estudiante} tiene {notas[materia][estudiante]} en {materia}")

        elif rol == "estudiante":
            if user in notas[materia]:
                print(f"\n📌 Tus notas en {materia} son: {notas[materia][user]}")
            else:
                print("\n📌 No hay notas registradas para esta materia.")

else: print(f"Usuario o contraseña incorrecta")

