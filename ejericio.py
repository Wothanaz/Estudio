nombre = input("Bienvenido, cual es tu nombre")

print('Bienvenido ', nombre)
print('-------------------')

numero = input('Cuantos productos vas a llevar?')


while not numero.isdigit():
    print("Por favor introducir un numero")
    numero = input()
else:
    print("Pagaras ", numero, " productos")
print("-----------------------")

numero = int(numero)

precio = []
precio_ac = 0
for i in range(numero):
    precio = input("Por favor introduce el valor del producto numero", i+1)
    print("El producto cuesta $:", precio)
    precio_ac += precio

print("Pagaras un total de $", precio_ac)
