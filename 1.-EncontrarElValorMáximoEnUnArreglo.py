#Crea un arreglo con 7 números de tu elección y escribe un código que encuentre y muestre el valor mínimo.

# Crear un arreglo con números
numeros = [43, 60, 4, 26, 4, 72]

# Inicializar una variable para almacenar el valor mínimo
mínimo = numeros[0]

# Recorrer el arreglo para encontrar el mínimo
for numero in numeros:
 if numero > mínimo:
    mínimo = numero

# Mostrar el valor máximo
print("El valor máximo es:", mínimo)