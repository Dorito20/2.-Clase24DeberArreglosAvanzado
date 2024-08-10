#Crea un arreglo con números del 1 al 10. Luego, invierte el arreglo y muestra el resultado.

# Crear un arreglo con números del 1 al 10
numeros = list(range(1, 11))

# Invertir el arreglo usando slicing
numeros_invertidos = numeros[::-1]

# Mostrar el arreglo invertido
print("El arreglo invertido es:", numeros_invertidos)
