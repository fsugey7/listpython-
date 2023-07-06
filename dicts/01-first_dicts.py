# Un diccionario es como una lista, pero más general, es decir, en un diccinario los índices pueden ser casi de cualquier tipo.
# En los diccionarios los índices son llamados *llaves* o *keys* y tiene asociado sus respectivos valores.

# Ejemplo:
empty_dicts = {} # Crea un diccionario vacío

english_to_spanish = {"one":"uno","two":"dos"}

# Los elementos se agregan en pares, es decir, llave-valor
english_to_spanish["hello"] = "hola"
english_to_spanish["bye"] = "chao"

print(english_to_spanish)

# Para acceder a el valor de una llave en específico usamos la notacíon con [].
print(english_to_spanish["one"])

# El largo de un diccionario se puede obtener con la función len(), igual que con las listas.
print(len(english_to_spanish)) # => 4