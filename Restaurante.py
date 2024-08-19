class Restaurante:
    def __init__(self, nombre_plato="", tipo_cocina="", precio=0.0, tiempo_preparacion=0, estado=""):
        self.estado = "NO ATENDIDO"
        self.nombre_plato = nombre_plato
        self.tipo_cocina = tipo_cocina
        self.precio = precio
        self.tiempo_preparacion = tiempo_preparacion
        self.calcular_categoria_precio()

    def calcular_categoria_precio(self):
        if self.precio < 10:
            self.categoria_precio = "Económico"
        elif 10 <= self.precio <= 20:
            self.categoria_precio = "Moderado"
        else:
            self.categoria_precio = "Caro"

    def cambiar_estado(self):
        self.estado = "ATENDIDO"
        return self.estado

    def entrada_datos(self):
        self.nombre_plato = input("Nombre del Plato: ")
        self.tipo_cocina = input("Tipo de Cocina (Ej: Italiana, Mexicana): ")
        self.precio = float(input("Precio del Plato: "))
        self.tiempo_preparacion = int(input("Tiempo de Preparación en minutos: "))
        self.calcular_categoria_precio()

    def muestra_datos(self):
        print(f"Nombre del Plato: {self.nombre_plato}")
        print(f"Tipo de Cocina: {self.tipo_cocina}")
        print(f"Precio: ${self.precio}")
        print(f"Categoría de Precio: {self.categoria_precio}")
        print(f"Tiempo de Preparación: {self.tiempo_preparacion} minutos")
        print(f"Estado: {self.estado}")

# Ejemplo de uso
pedido = Restaurante()  # Se puede crear la instancia sin valores iniciales
pedido.entrada_datos()  # Se piden los datos al usuario
pedido.cambiar_estado()  # Cambia el estado a "ATENDIDO"
pedido.muestra_datos()  # Muestra todos los datos del pedido
