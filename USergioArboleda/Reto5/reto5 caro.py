
prodtos = {"código": [1,2,3,4,5,6,7,8,9,10], \
    "nombre": ["Manzanas","Limones", "Peras", "Arandanos", "Tomates", "Fresas", "Helado", "Galletas", "Chocolates", "Jamon"], \
        "precio":[5000.0, 2300.0, 2700.0, 9300.0, 2100.0, 4100.0, 4500.0, 500.0, 3500.0, 15000.0], \
            "inventario": [25, 15, 33, 5, 42, 3, 41, 8, 80, 10]}
    
def precioMayor():
    mayor = 0
    for i in range(0, len(prodtos["precio"])):
        if mayor < prodtos["precio"][i]:
            mayor = prodtos["precio"][i]
    
    indice = prodtos["precio"].index(mayor)

    return prodtos["nombre"][indice]
    
def precioMenor():
    menor = prodtos["precio"][0]
    for i in range(0, len(prodtos["precio"])):
        if menor > prodtos["precio"][i]:
            menor = prodtos["precio"][i]
    indice = prodtos["precio"].index(menor)
    return prodtos["nombre"][indice]

def precioPromedio():
    suma = 0
    for i in range(0, len(prodtos["precio"])):
        suma += prodtos["precio"][i]
    promedio = suma/len(prodtos["precio"])
    return round(promedio,1)

def totalInventario():
    suma = 0
    for i in range(0, len(prodtos["precio"])):
        suma += prodtos["precio"][i]*prodtos["inventario"][i]
    return suma

def agregar(codigo, nombre, precio, inventario):
    if not codigo in prodtos["código"]:
        prodtos["código"].append(codigo)
        prodtos["nombre"].append(nombre)
        prodtos["precio"].append(precio)
        prodtos["inventario"].append(inventario)
        print(precioMayor(), precioMenor(), precioPromedio(), totalInventario())
    else:
        print("ERROR")

def borrar(codigo):
    if codigo in prodtos["código"]:
        indice = prodtos["código"].index(codigo)
        del prodtos["código"][indice]
        del prodtos["nombre"][indice]
        del prodtos["precio"][indice]
        del prodtos["inventario"][indice]
        print(precioMayor(), precioMenor(), precioPromedio(), totalInventario())
    else:
        print("ERROR")

def actualizar(codigo, nombre, precio, inventario):
    if codigo in prodtos["código"]:
        if nombre in prodtos["nombre"]:
            indice = prodtos["código"].index(codigo)
            prodtos["nombre"][indice] = nombre
            prodtos["precio"][indice] = precio
            prodtos["inventario"][indice] = inventario
            print(precioMayor(), precioMenor(), precioPromedio(), totalInventario())
        else:
            print("ERROR")
    else:
        print("ERROR")

operacion = input()
codigo, nombre, precio, prod = input().split()
codigo = int(codigo)
precio = float(precio)
prod = int(prod)

if operacion.upper() == "AGREGAR":
    agregar(codigo, nombre, precio, prod)
elif operacion.upper() == "BORRAR":
    borrar(codigo)
elif operacion.upper() == "ACTUALIZAR":
    actualizar(codigo, nombre, precio, prod)