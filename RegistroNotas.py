print("Selecciona la opcion que te corresponda:")
select = input("a)Estudiante\nb)Profesor")
match select:
    case "a":
        print("Estudiante")
    case "b":
        print("Profesor")


print("Por favor, registra el correo y la contraseña:")
userCorrectly = input("Digite el correo que desea registrar: ")
passwordCorrectly = input("Digite la contraseña que desea registrar: ")

print("Inisia sesion ")

user = input("Ingrese usuario: ")
password = input("Ingrese contraseña: ")

if user == userCorrectly and password == passwordCorrectly:
    print("Bienvenido " + user)
  
       
else:
    print("Error: Correo o contraseña incorrectos ")
    
