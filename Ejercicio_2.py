# de una lista de n numeros que ingresa el usuario, sacar el maximo, minimo, promedio y sumatoria
print("Cuantos numeros quieres tener en tu lista?")

numero = input()
while not numero.isdigit():
    print("Por favor introducir un numero")
    numero = input()

print("Tu lista tendra ", numero, " numeros")
print("____________________-")
print("vamos a ingresar los nùmeros de la lista")
lista_numero = []
for i in range(int(numero)):
    num_i = input()
    while not numero.isdigit():
        print("Por favor introducir un numero")
        num_i = input()
    else:
        print("Ingresaste el número ", num_i)
        lista_numero.append(int(num_i))

print("____________________-")
print("_esta es la lista que ingresaste")
print(lista_numero)
promedio = sum(lista_numero)/int(numero)

print("el màximo es: ", max(lista_numero))
print("el minimo es: ", min(lista_numero))
print("la suma de la lista es ", sum(lista_numero))
print("el valor promedio es: ", promedio)

               