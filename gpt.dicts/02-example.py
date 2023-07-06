# Crear un diccionario vacío 
diccionario = {}

# Create a dictionary with initial values.
dic ={'name': 'john', 'age': 25, 'city': 'london'}

# Access a value through a key
print(dic['name']) # Imprime john
print(dic['age']) # Imprime 25
print(dic['city']) # Imprime london

# Modificar un valor existente

dic['age'] = 30 # Se accede también mediante la llave
print('-------------')
print(dic['age']) # Se imprime 30 el nuevo valor

# Agregar un nuevo par llave-valor
dic['hero'] = 'Batman'
print('---------------')
print(dic)

# Eliminar un par llave-valor madiante la llave
del dic['age']
print('-----------')
print(dic)

# Revisar si existe la llave en el diccionario
if "hero" in dic:
    print(f"El héroe en acción es {dic['hero']}")

# Obtener el listado de llaves y valores
keys = dic.keys()
values = dic.values()

print(keys)
print(values)

# El método items ns entrega una lista con los pares llave valor que podemos después recorrer
items = dic.items()
print(items)

# Recorre el arreglo con for e items:
for key, value in dic.items():
    print(key, ':', value)

# Otra forma de recorrer el diccionario:
for key in dic.keys():
    print(key, ':', dic[key])