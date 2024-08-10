#Crea un arreglo con una lista de palabras. Luego, cuenta cuántas veces aparece una palabra específica en el arreglo y muestra el resultado.

# Crear un arreglo con una lista de palabras
palabras = ["niño, niña", "dama", "cereza", "niño, niña", "durazno", "manzana", "dama" , "niño, niña"]

# Palabra a buscar
palabra_buscar = "niño, niña"

# Contador para contar cuántas veces aparece la palabra
contador = 0

# Recorrer el arreglo para contar la aparición de la palabra
for palabra in palabras:
    if palabra == palabra_buscar:
        contador += 1

# Mostrar el resultado
print(f"La palabra '{palabra_buscar}' aparece {contador} veces en la lista.")