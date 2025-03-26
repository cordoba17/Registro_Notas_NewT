import json
import os

# Archivo donde se guardarán las notas
archivo_notas = "notas.json"

# 📌 Cargar las notas desde el archivo si existe, asegurando que los valores sean numéricos
if os.path.exists(archivo_notas):
    with open(archivo_notas, "r") as file:
        try:
            notas = json.load(file)
            # Convertir todas las notas a float si no lo son
            for materia in notas:
                for estudiante in notas[materia]:
                    notas[materia][estudiante] = [float(n) for n in notas[materia][estudiante]]
        except json.JSONDecodeError:
            notas = {"Matemáticas": {}, "Inglés": {}, "Química": {}}
else:
    notas = {"Matemáticas": {}, "Inglés": {}, "Química": {}}

# Selección de usuario
print("Selecciona la opción que te corresponda:")
select = input("a) Estudiante\nb) Profesor\n> ").strip().lower()

if select == "a":
    print("\nBienvenido Estudiante")
    rol = "estudiante"
elif select == "b":
    print("\nBienvenido Profesor")
    rol = "profesor"
else:
    print("\n❌ Opción no válida. Saliendo del programa.")
    exit()

# Registro de usuario
print("\nPor favor, registra el correo y la contraseña:")
userCorrectly = input("Digite el correo que desea registrar: ").strip()
passwordCorrectly = input("Digite la contraseña que desea registrar: ").strip()

# Inicio de sesión
while True:
    print("\nInicia sesión")
    user = input("Ingrese usuario: ").strip()
    password = input("Ingrese contraseña: ").strip()

    if user == userCorrectly and password == passwordCorrectly:
        print(f"\n✅ Bienvenido {user}")
        break
    else:
        print("❌ Usuario o contraseña incorrecta. Inténtalo de nuevo.")

while True:
    print("\n📚 MENÚ DE MATERIAS")
    print("1. Matemáticas")
    print("2. Inglés")
    print("3. Química")
    print("4. Salir")

    opcion = input("Selecciona una materia (1-4): ").strip()

    if opcion == "1":
        materia = "Matemáticas"
    elif opcion == "2":
        materia = "Inglés"
    elif opcion == "3":
        materia = "Química"
    elif opcion == "4":
        print("\n👋 Saliendo del programa. ¡Hasta luego!")

        # 📌 Guardar las notas en el archivo antes de salir
        with open(archivo_notas, "w") as file:
            json.dump(notas, file, indent=4)

        break
    else:
        print("\n❌ Opción no válida. Intenta de nuevo.")
        continue

    if rol == "profesor":
        estudiante = input("\nIngrese el nombre del estudiante: ").strip()
        try:
            nota = float(input(f"Ingrese la nota de {estudiante} en {materia}: ").strip())  # Convertir a número
        except ValueError:
            print("❌ Error: La nota debe ser un número.")
            continue

        # 📌 Si el estudiante no tiene notas en la materia, inicializamos una lista
        if estudiante not in notas[materia]:
            notas[materia][estudiante] = []

        # Agregar la nueva nota a la lista
        notas[materia][estudiante].append(nota)

        # 📌 Asegurar que todas las notas sean flotantes antes de guardar
        notas[materia][estudiante] = [float(n) for n in notas[materia][estudiante]  ]

        # 📌 Guardar automáticamente cada vez que se agregan notas
        with open(archivo_notas, "w") as file:
            json.dump(notas, file, indent=4)

        print(f"\n✅ Nota registrada: {estudiante} tiene {notas[materia][estudiante]} en {materia}")

    elif rol == "estudiante":
        if user in notas[materia]:
            notas_estudiante = [float(n) for n in notas[materia][user]]  # Convertir notas a float

            promedio = sum(notas_estudiante) / len(notas_estudiante) if notas_estudiante else 0
            print(f"\n📌 Tus notas en {materia} son: {notas_estudiante}")
            print(f"📊 Tu promedio en {materia} es: {promedio:.2f}")
        else:
            print("\n📌 No hay notas registradas para esta materia.")
