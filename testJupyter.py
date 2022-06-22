#Build a data base using dictionaries

# while(cola != len(lista)-1):
#     if indiceLista != cola:
#         carrete.append(lista[indiceLista])
#         indiceLista += 1
        
    # else:
    #     cabeza += 1
    #     cola += 1
    #     indiceLista = cabeza

dictionary = {"código": [1,2,3,4,5,6,7,8,9,10], \
    "nombre": ["Manzanas","Limones", "Peras", "Arandanos", "Tomates", "Fresas", "Helado", "Galletas", "Chocolates", "Jamon"], \
        "precio":[5000, 2300, 2700, 9300, 2100, 4100, 4500, 500, 3500, 15000], \
            "inventario": [25, 15, 33, 5, 42, 3, 41, 8, 80, 10]}

print([dictionary["nombre"].index("Fresas")])

# copia = lista

# print(lista)
# print(copia)

# op = int(input("Escoja un numero a buscar: "))
# cont = 0
# defect = 0

# for i in range(len(copia)):
#     for j in range(len(lista)):
#         if i == j:
#             cont += 1
#             if cont > 1:
#                 defect += 1
#                 cont = 0

# print(defect)



