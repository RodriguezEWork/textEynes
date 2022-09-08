import random

def generar_lista():
    diccionario = {}
    for i in range(10):
        diccionario[i] = random.randrange(1,100, 1)
    return diccionario

diccionario = generar_lista()
print (diccionario)

def realizar_acciones(diccionario):
    mas_vieja = max(diccionario, key = diccionario.get)
    mas_joven = min(diccionario, key = diccionario.get)
    ordenado = sorted(diccionario.values(), reverse=True)
    print('La persona mas joven es ' , mas_joven)
    print('La persona mas vieja es ' , mas_vieja)
    print(ordenado)

realizar_acciones(diccionario)