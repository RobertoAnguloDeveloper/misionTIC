
class Tienda:
    productos = {"código": [1,2,3,4,5,6,7,8,9,10], \
        "nombre": ["Manzanas","Limones", "Peras", "Arandanos", "Tomates", "Fresas", "Helado", "Galletas", "Chocolates", "Jamon"], \
            "precio":[5000.0, 2300.0, 2700.0, 9300.0, 2100.0, 4100.0, 4500.0, 500.0, 3500.0, 15000.0], \
                "inventario": [25, 15, 33, 5, 42, 3, 41, 8, 80, 10]}
    
    def precioMayor(self,):
        mayor = 0
        for i in range(0, len(self.productos["precio"])):
            if mayor < self.productos["precio"][i]:
                mayor = self.productos["precio"][i]
        
        indice = self.productos["precio"].index(mayor)

        return self.productos["nombre"][indice]
    
    def precioMenor(self,):
        menor = self.productos["precio"][0]
        for i in range(0, len(self.productos["precio"])):
            if menor > self.productos["precio"][i]:
                menor = self.productos["precio"][i]
        indice = self.productos["precio"].index(menor)
        return self.productos["nombre"][indice]

    def precioPromedio(self,):
        suma = 0
        for i in range(0, len(self.productos["precio"])):
            suma += self.productos["precio"][i]
        promedio = suma/len(self.productos["precio"])
        return round(promedio,1)

    def totalInventario(self,):
        suma = 0
        for i in range(0, len(self.productos["precio"])):
            suma += self.productos["precio"][i]*self.productos["inventario"][i]
        return suma
    
    def agregar(self,codigo, nombre, precio, inventario):
        if not codigo in self.productos["código"]:
            self.productos["código"].append(codigo)
            self.productos["nombre"].append(nombre)
            self.productos["precio"].append(precio)
            self.productos["inventario"].append(inventario)
            print(self.precioMayor(), self.precioMenor(), self.precioPromedio(), self.totalInventario())
        else:
            print("ERROR")
    
    def borrar(self, codigo):
        if codigo in self.productos["código"]:
            indice = self.productos["código"].index(codigo)
            del self.productos["código"][indice]
            del self.productos["nombre"][indice]
            del self.productos["precio"][indice]
            del self.productos["inventario"][indice]
            print(self.precioMayor(), self.precioMenor(), self.precioPromedio(), self.totalInventario())
        else:
            print("ERROR")

    def actualizar(self, codigo, nombre, precio, inventario):
        if codigo in self.productos["código"]:
            if nombre in self.productos["nombre"]:
                indice = self.productos["código"].index(codigo)
                self.productos["nombre"][indice] = nombre
                self.productos["precio"][indice] = precio
                self.productos["inventario"][indice] = inventario
                print(self.precioMayor(), self.precioMenor(), self.precioPromedio(), self.totalInventario())
            else:
                print("ERROR")
        else:
            print("ERROR")

    def toString(self):
        print("\n")
        for i in range(0, len(self.productos["código"])):
            print(self.productos["código"][i],self.productos["nombre"][i]\
                ,self.productos["precio"][i]\
                    ,self.productos["inventario"][i])

tienda = Tienda()

operacion = input()
codigo, nombre, precio, productos = input().split()
codigo = int(codigo)
precio = float(precio)
productos = int(productos)

if operacion.upper() == "AGREGAR":
    tienda.agregar(codigo, nombre, precio, productos)
elif operacion.upper() == "BORRAR":
    tienda.borrar(codigo)
elif operacion.upper() == "ACTUALIZAR":
    tienda.actualizar(codigo, nombre, precio, productos)