class Joyeria:
    def __init__(self, tipo_piedra="", tipo_metal="", precio_compra=0.0):
        self.tipo_piedra = tipo_piedra
        self.tipo_metal = tipo_metal
        self.marca_piedra = "Brillo Puro"
        self.marca_metal = "Oro Fino"
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.50

    def recibir_datos(self):
        tipo_piedra = int(input("Seleccione el tipo de piedra (1: Diamante, 2: Zafiro): "))
        if tipo_piedra == 1:
            self.tipo_piedra = "Diamante"
        elif tipo_piedra == 2:
            self.tipo_piedra = "Zafiro"
        else:
            print("Opción no válida.")
        
        tipo_metal = input("Seleccione el tipo de metal (oro o plata): ").lower()
        if tipo_metal == "oro":
            self.tipo_metal = "Oro"
        elif tipo_metal == "plata":
            self.tipo_metal = "Plata"
        else:
            print("Opción no válida.")
        
        self.precio_compra = float(input("Ingrese el precio de compra: "))
        self.precio_venta = self.calcular_precio_venta()

    def mostrar_datos(self):
        print("\nDetalles de la joya registrada:")
        print(f"Marca de Piedra: {self.marca_piedra}")
        print(f"Tipo de Piedra: {self.tipo_piedra}")
        print(f"Marca de Metal: {self.marca_metal}")
        print(f"Tipo de Metal: {self.tipo_metal}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")


# Ejemplo de uso
joya1 = Joyeria()
joya1.recibir_datos()
joya1.mostrar_datos()

joya2 = Joyeria()
joya2.recibir_datos()
joya2.mostrar_datos()
