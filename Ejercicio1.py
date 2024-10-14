class Rutina:
    def __init__(self): 
        self.actividades = {}  
        self.relaciones = {}    
    
    def agregar_actividad(self, actividad, tiempo):
        self.actividades[actividad] = tiempo 
        self.relaciones[actividad] = []  
    
    def agregar_relacion(self, actividad, *actividades_dependientes):
        if actividad in self.relaciones:
            self.relaciones[actividad].extend(actividades_dependientes)  
    
    def mostrar_rutina(self):
        for actividad, tiempo in self.actividades.items():
            print(f"{actividad}: {tiempo} minutos")
            if self.relaciones[actividad]:
                print(f"  Dependencias: {', '.join(self.relaciones[actividad])}")

    def buscar_actividad(self, actividad):
        if actividad in self.actividades:
            tiempo = self.actividades[actividad]
            return f"{actividad} se realiza durante {tiempo} minutos."
        return f"{actividad} no se encuentra en la rutina."

    def tiempo_total(self):
        total_minutos = sum(self.actividades.values())
        return f"Tiempo total de actividades: {total_minutos} minutos."


rutina = Rutina()

rutina.agregar_actividad('Despertar', 10)  
rutina.agregar_actividad('Alistarme', 5)
rutina.agregar_actividad('Bañarme', 7)
rutina.agregar_actividad('Comer', 12)
rutina.agregar_actividad('Tomar bus', 90)
rutina.agregar_actividad('Llegar a la universidad', 3)
rutina.agregar_actividad('Ir a biblioteca', 4)
rutina.agregar_actividad('Ir a clases de matemáticas', 8)
rutina.agregar_actividad('Tomar microbus', 180)

rutina.agregar_relacion('Despertar', 'Alistarme', 'Bañarme')
rutina.agregar_relacion('Alistarme', 'Comer', 'Tomar bus')
rutina.agregar_relacion('Tomar bus', 'Llegar a la universidad')
rutina.agregar_relacion('Llegar a la universidad', 'Ir a clases de matemáticas', 'Ir a biblioteca')

rutina.mostrar_rutina()

print(rutina.buscar_actividad('Comer'))  
print(rutina.buscar_actividad('Estudiar'))  

print(rutina.tiempo_total())
