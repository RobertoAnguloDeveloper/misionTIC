n = int(input())
lista = []
for i in range(n):
    listaTemp = []
    w, x, y, z, a = input().split()
    w = int(w)
    x = int(x)
    y = int(y)
    z = int(z)
    a = int(a)
    listaTemp.append([w,x,y,z,a])
    lista.append(listaTemp[0])

print(lista)

# matriz = [["n00","n01","n02"],
#          ["n10","n11","n12"],
#          ["n20","n21","n22"]]

# matrizInv = []
# print("**********************")
# print("Matriz sin invertir")
# print("**********************")
# for i in range(len(matriz[0])) :
#     print(matriz[i])

# print("**********************")
# print("Matriz invertida")
# print("**********************")
# for i in range(len(matriz[0])) :
#     matrizInv.append([])
#     for j in range(len(matriz[0])) :
#         matrizInv[i].append(matriz[j][i])

# for i in range(len(matriz[0])) :
#     print(matrizInv[i])

# import math

# numero = float(input("Ingrese el numero a hallar la raiz cuarta: "))

# raiz = math.pow(numero,1/4)

# print("La raiz cuarta de",numero,"es",round(raiz,2))

# radio = float(input("Ingrese el radio del círculo: "))

# area = math.pi * math.pow(radio,2)

# print("El área del círculo es:",round(area,2))

# nombreProducto = input("Ingrese el nombre del producto: ")
# costeProduccion = float(input("Ingrese el coste de produccion: "))

# precioVenta = costeProduccion + costeProduccion*1.2 + costeProduccion*0.15

# print("El precio de venta del producto",nombreProducto,"es de $",round(precioVenta,2))
