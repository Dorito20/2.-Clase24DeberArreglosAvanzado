#Crea un arreglo con palabras que incluyan algunas duplicadas. Luego, elimina las palabras duplicadas y muestra el resultado.

# Crear un arreglo con palabras, incluyendo duplicadas
palabras = ["vida", "oveja", "cereza", "flor", "año", "agua", "sociedad", "cereza", "flor", "agua", "oveja", "flor"]

# Crear un nuevo arreglo para almacenar las palabras sin duplicados
palabras_sin_duplicados = []

# Recorrer el arreglo y agregar las palabras no duplicadas al nuevo arreglo
for palabra in palabras:
    if palabra not in palabras_sin_duplicados:
        palabras_sin_duplicados.append(palabra)

# Mostrar el nuevo arreglo sin duplicados
print("Arreglo sin duplicados:", palabras_sin_duplicados)
