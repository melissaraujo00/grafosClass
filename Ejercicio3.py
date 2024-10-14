class Comercial:
    def __init__(self):
        self.grafo = {}

    def agregar_comercial(self, comercial):
        if comercial not in self.grafo:
            self.grafo[comercial] = {}

    def agregar_categoria(self, comercial, categoria):
        if comercial in self.grafo:
            if categoria not in self.grafo[comercial]:
                self.grafo[comercial][categoria] = []
            else:
                print(f"La categoría '{categoria}' ya existe en '{comercial}'.")
        else:
            print(f"El comercio '{comercial}' no existe. Primero, agrégalo.")

    def agregar_producto(self, comercial, categoria, producto):
        if comercial in self.grafo:
            if categoria in self.grafo[comercial]:
                self.grafo[comercial][categoria].append(producto)
            else:
                print(f"La categoría '{categoria}' no existe en '{comercial}'.")
        else:
            print(f"El comercio '{comercial}' no existe. Primero, agrégalo.")

    def buscar_producto(self, producto):
        for comercial, categorias in self.grafo.items():
            for categoria, productos in categorias.items():
                if producto in productos:
                    return f"{producto} pertenece al comercio '{comercial}' en la categoría: '{categoria}'."
        return f"{producto} no se encuentra en ningún comercio."

    def buscar_categoria(self, comercial, categoria):
        if comercial in self.grafo:
            if categoria in self.grafo[comercial]:
                return f"Productos en la categoría '{categoria}' del comercio '{comercial}': {', '.join(self.grafo[comercial][categoria])}."
            return f"La categoría '{categoria}' no existe en el comercio '{comercial}'."
        return f"El comercio '{comercial}' no existe."

    def mostrar_grafo(self):
        for comercial, categorias in self.grafo.items():
            print(f"Comercio: {comercial}")
            for categoria, productos in categorias.items():
                print(f"  Categoría: {categoria} -> Productos: {', '.join(productos)}")



grafo = Comercial()

grafo.agregar_comercial('Casa Comercial')

grafo.agregar_categoria('Casa Comercial', 'Electrodomésticos')
grafo.agregar_categoria('Casa Comercial', 'Muebles')
grafo.agregar_categoria('Casa Comercial', 'Tecnología')

grafo.agregar_producto('Casa Comercial', 'Electrodomésticos', 'Refrigeradora')
grafo.agregar_producto('Casa Comercial', 'Electrodomésticos', 'Lavadora')
grafo.agregar_producto('Casa Comercial', 'Electrodomésticos', 'Microondas')

grafo.agregar_producto('Casa Comercial', 'Muebles', 'Sofá')
grafo.agregar_producto('Casa Comercial', 'Muebles', 'Mesa')
grafo.agregar_producto('Casa Comercial', 'Muebles', 'Silla')

grafo.agregar_producto('Casa Comercial', 'Tecnología', 'Teléfono')
grafo.agregar_producto('Casa Comercial', 'Tecnología', 'Tablet')
grafo.agregar_producto('Casa Comercial', 'Tecnología', 'Laptop')

grafo.mostrar_grafo()

print(grafo.buscar_categoria('Casa Comercial', 'Decoración'))  
print(grafo.buscar_categoria('Casa Comercial', 'Muebles'))

print(grafo.buscar_producto('Cocina'))         
print(grafo.buscar_producto('Silla'))           
