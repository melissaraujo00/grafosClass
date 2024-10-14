class GrafoMusical:
    def __init__(self):
        self.grafo = {}  

    def agregar_genero(self, genero):
        if genero not in self.grafo:
            self.grafo[genero] = []  

    def agregar_artista(self, genero, artista):
        if genero in self.grafo:
            self.grafo[genero].append(artista)  
        else:
            print(f"El género '{genero}' no existe. Primero, agréguelo.")
    
    def buscar_artista(self, artista):
        for genero, artistas in self.grafo.items():
            if artista in artistas:
                return f"{artista} pertenece al género: {genero}."
        return f"{artista} no se encuentra en ningún género."


    def mostrar_grafo(self):
        for genero, artistas in self.grafo.items():
            print(f"Género: {genero} -> Artistas: {', '.join(artistas)}")


grafo = GrafoMusical()

grafo.agregar_genero('Bedroom Pop')

grafo.agregar_artista('Bedroom Pop', 'Cavetown')
grafo.agregar_artista('Bedroom Pop', 'Clairo')
grafo.agregar_artista('Bedroom Pop', 'Beabadoobee')

grafo.mostrar_grafo()

print(grafo.buscar_artista('Madonna'))  
print(grafo.buscar_artista('Clairo')) 


