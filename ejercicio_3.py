# entre 0 y 5 - primera infancia
# entre 6 y 12 - niñez
# entre 13 y 16 adolescencia
# 18 o mas adulto

print("introduce una edad")
edad = input() 
while not edad.isdigit():
    print("Por favor introducir un numero")
    edad = input()
else:
    edad = int(edad)
    print("Ingresaste una edad de ", edad, " años")


print("--------------")
if edad <=5:
    print ("El usuario está en la primera infancia")
elif edad>=6 and edad<=12:
    print("El usuario está en la niñez")
elif edad>=13 and edad<=17:
    print("El usuario está en la niñez")
else:
    print("El usuario está en la adultez")
    print("---------------")
    print("Por Favor Ingresa tus apellidos")
    apellido = input()
    print("Tus apellidos son :", apellido)
    print("Por Favor ingresa tu nombre:")
    nombre = input()
    print("Tu nombre es : ", nombre)
    print("Por Favor ingresa tu correo:")
    correo = input()
    print("Tu correo es: ", correo)

parametros = ['Edad', 'Apellidos', 'Nombre', 'Correo']
variables = [edad, apellido, nombre, correo]

usuario = dict(zip(parametros, variables))
print(usuario)

