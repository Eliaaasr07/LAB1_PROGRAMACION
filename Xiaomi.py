class Xiaomi:
    def __init__(self):
        self.marca = "Xiaomi"
        self.modelo = input("Ingrese el modelo de Xiaomi: ")
        self.color = input("Ingrese el color del teléfono: ")
        self.capacidad_almacenamiento = input("Ingrese la capacidad de almacenamiento (e.g., 128GB): ")
        self.ram = input("Ingrese la memoria RAM (e.g., 6GB): ")
        self.tipo_procesador = input("Ingrese el tipo de procesador: ")
        self.precio_compra = float(input("Ingrese el precio de compra del teléfono: "))
        self.precio_venta = self.calcular_precio_venta()
        self.sistema_operativo = "MIUI"  # Sistema operativo predeterminado para Xiaomi

    def calcular_precio_venta(self):
        return self.precio_compra * 1.5

    def mostrar_datos(self):
        print("\nCaracterísticas del teléfono Xiaomi:")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")
        print(f"Capacidad de Almacenamiento: {self.capacidad_almacenamiento}")
        print(f"Memoria RAM: {self.ram}")
        print(f"Tipo de Procesador: {self.tipo_procesador}")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Ejemplo de uso
print("Registro del primer teléfono Xiaomi:")
xiaomi1 = Xiaomi()
xiaomi1.mostrar_datos()

print("\nRegistro del segundo teléfono Xiaomi:")
xiaomi2 = Xiaomi()
xiaomi2.mostrar_datos()
