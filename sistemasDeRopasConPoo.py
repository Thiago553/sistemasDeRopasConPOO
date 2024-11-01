from abc import ABC, abstractmethod


class Producto(ABC):
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    @abstractmethod
    def mostrar_info(self):
        pass

    def get_precio(self):
        return self.__precio

    def get_nombre(self):
        return self.__nombre

class Ropa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def mostrar_info(self):
        return f"{self.get_nombre()} - Talla: {self.__talla}, Precio: ${self.get_precio()}"


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, manga_larga):
        super().__init__(nombre, precio, talla)
        self.__manga_larga = manga_larga

    def mostrar_info(self):
        tipo_manga = "Manga Larga" if self.__manga_larga else "Manga Corta"
        return f"Camisa: {super().mostrar_info()}, Tipo de Manga: {tipo_manga}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo):
        super().__init__(nombre, precio, talla)
        self.__tipo = tipo

    def mostrar_info(self):
        return f"Pantalón: {super().mostrar_info()}, Tipo: {self.__tipo}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, material):
        super().__init__(nombre, precio, talla)
        self.__material = material

    def mostrar_info(self):
        return f"Zapato: {super().mostrar_info()}, Material: {self.__material}"

class Carrito:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_carrito(self):
        for idx, producto in enumerate(self.__productos):
            print(f"{idx + 1}. {producto.mostrar_info()}")

    def calcular_total(self):
        total = sum(producto.get_precio() for producto in self.__productos)
        return total

class Tienda:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        for idx, producto in enumerate(self.__productos):
            print(f"{idx + 1}. {producto.mostrar_info()}")

    def procesar_compra(self, seleccion, carrito):
        if 0 <= seleccion < len(self.__productos):
            producto = self.__productos[seleccion]
            carrito.agregar_producto(producto)
            print(f"Producto agregado al carrito: {producto.mostrar_info()}")
        else:
            print("Selección no válida.")


def main():
    tienda = Tienda()
    carrito = Carrito()

    tienda.agregar_producto(Camisa("Camisa de Rayas", 29.99, "M", True))
    tienda.agregar_producto(Pantalon("Pantalón Casual", 39.99, "L", "Chino"))
    tienda.agregar_producto(Zapato("Zapato Deportivo", 49.99, "42", "Sintético"))

    print("Bienvenido a la tienda de ropa!")
    while True:
        print("\nProductos disponibles:")
        tienda.mostrar_productos()
        seleccion = int(input("Seleccione un producto para comprar (o 0 para finalizar): ")) - 1
        if seleccion == -1:
            break
        tienda.procesar_compra(seleccion, carrito)

    print("\nResumen de su compra:")
    carrito.mostrar_carrito()
    print(f"Total a pagar: ${carrito.calcular_total():.2f}")
    print("Gracias por su compra!")


if __name__ == "__main__":
    main()
