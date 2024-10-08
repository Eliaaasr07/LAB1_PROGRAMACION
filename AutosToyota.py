class Toyota:
    def __init__(self):
        self.marca = "Toyota"
        self.modelo = input("Ingrese el modelo de Toyota: ")
        self.año = input("Ingrese el año del auto: ")
        self.color = input("Ingrese el color del auto: ")
        self.tipo_combustible = input("Ingrese el tipo de combustible (Gasolina/Diesel/Eléctrico): ")
        self.transmision = input("Ingrese el tipo de transmisión (Automática/Manual): ")
        self.motor = input("Ingrese el tipo de motor (e.g., 2.0L): ")
        self.origen = input("Ingrese el origen del auto (Nacional/Importado): ")
        self.precio_compra = float(input("Ingrese el precio de compra del auto: "))
        self.precio_venta = self.calcular_precio_venta()
        self.ruedas = 4  
        self.capacidad = 5  

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_datos(self):
        print("\nCaracterísticas del vehículo Toyota:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de Combustible: {self.tipo_combustible}")
        print(f"Transmisión: {self.transmision}")
        print(f"Motor: {self.motor}")
        print(f"Origen: {self.origen}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Ejemplo de uso
print("Registro del primer Toyota:")
toyota1 = Toyota()
toyota1.mostrar_datos()

print("\nRegistro del segundo Toyota:")
toyota2 = Toyota()
toyota2.mostrar_datos()
