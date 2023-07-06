# Si utilizamos un loop for para recorrer un diccionario, el for va a recorrer las laves del diccionario y podemos utilizar las laves para acceder a lo valores.

some_dict = {
    "name":"Sugey",
    "lastname": "Flores",
    "weight": 52,
    "height": 1.65
}

for key in some_dict:
    print(key, some_dict)