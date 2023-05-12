import datetime

class Producto:
    def __init__(self, nombre, proveedor, fecha_caducidad, fecha_entrada, detalles, precio, unidades):
        self.nombre = nombre
        self.proveedor = proveedor
        self.fecha_caducidad = fecha_caducidad
        self.fecha_entrada = fecha_entrada
        self.detalles = detalles
        self.precio = precio
        self.unidades = unidades

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

class Area:
    def __init__(self, nombre):
        self.nombre = nombre
        self.categorias = []

class Usuario:
    def __init__(self, id, nombre, edad, nivel):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.nivel = nivel

class Supermercado:
    def __init__(self):
        self.areas = []
        self.usuarios = []

    def agregar_area(self, area):
        self.areas.append(area)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, id):
        for usuario in self.usuarios:
            if usuario.id == id:
                return usuario
        return None

    def realizar_venta(self, usuario_id):
        usuario = self.buscar_usuario(usuario_id)
        if usuario is None:
            print("\nUsuario no encontrado.")
            return

        total = 0
        productos_seleccionados = []

        while True:
            print("\nÁreas disponibles:")
            for i, area in enumerate(self.areas):
                print(f"{i + 1}. {area.nombre}")

            area_seleccionada = int(input("\nSeleccione el área (0 para finalizar la compra): "))
            if area_seleccionada == 0:
                break

            area = self.areas[area_seleccionada - 1]

            print("\nCategorías disponibles:")
            for i, categoria in enumerate(area.categorias):
                print(f"{i + 1}. {categoria.nombre}")

            categoria_seleccionada = int(input("\nSeleccione la categoría: "))
            categoria = area.categorias[categoria_seleccionada - 1]

            print("\nProductos disponibles:")
            for i, producto in enumerate(categoria.productos):
                print(f"{i + 1}. {producto.nombre} - Precio: {producto.precio}")

            producto_seleccionado = int(input("\nSeleccione el producto: "))
            producto = categoria.productos[producto_seleccionado - 1]

            cantidad = int(input("\nIngrese la cantidad: "))
            total += producto.precio * cantidad
            productos_seleccionados.append((producto, cantidad))

        print("\nResumen de la compra:")
        for producto, cantidad in productos_seleccionados:
            print(f"{producto.nombre} - Cantidad: {cantidad} - Precio:$ {round(producto.precio * cantidad, 2)}")

        print(f"\nTotal a pagar:$ {total}")
        print("\n¡GRACIAS POR SU COMPRA!")
        
def main():
    supermercado = Supermercado()

    # Crear áreas y categorías iniciales
    area1 = Area("Alimentos")
    area2 = Area("Bebidas")
    supermercado.agregar_area(area1)
    supermercado.agregar_area(area2)

    categoria1 = Categoria("Frutas y Verduras")
    categoria2 = Categoria("Abarrotes")
    categoria3 = Categoria("Sodas y Jugos")
    categoria4 = Categoria("Bebidas Energizantes")
    area1.categorias.append(categoria1)
    area1.categorias.append(categoria2)
    area2.categorias.append(categoria3)
    area2.categorias.append(categoria4)

    # Crear productos
    producto1 = Producto("Manzanas", "Proveedor1", datetime.date(2023, 12, 31), datetime.date(2023, 5, 9), "Manzanas Rojas", 0.25, 200)
    producto2 = Producto("Peras", "Proveedor1", datetime.date(2023, 12, 31), datetime.date(2023, 5, 9), "Peras", 0.30, 200)
    producto3 = Producto("Bananas", "Proveedor1", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Bananas", 0.25, 200)
    producto4 = Producto("Naranjas", "Proveedor1", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Naranjas", 0.25, 200)
    producto5 = Producto("Uvas", "Proveedor1", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Uvas", 3.00, 150)
    producto6 = Producto("Tomate", "Proveedor1", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Tomates", 0.10, 500)
    producto7 = Producto("Papas", "Proveedor1",  datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Papas", 0.85, 500)
    producto8 = Producto("Cebolla", "Proveedor1",  datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Cebollas", 0.25, 500)
    producto9 = Producto("Zanahoria", "Proveedor1",  datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Zanahorias", 0.25, 500)
    producto10 = Producto("Chile verde", "Proveedor1",  datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Chile verde", 0.25, 450)    
    producto11 = Producto("Arroz precocido", "Proveedor2", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Arroz precocido", 0.75, 200)
    producto12 = Producto("Frijoles", "Proveedor2", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Frijoles", 1.10, 200)
    producto13 = Producto("Ázucar", "Proveedor2", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Ázucar", 0.65, 250)
    producto14 = Producto("Sal", "Proveedor2", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Sal", 0.25, 250)
    producto15 = Producto("Aceite", "Proveedor2", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Aceite", 1.25, 250)
    producto16 = Producto("Agua", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Agua", 0.50, 100)
    producto17 = Producto("Coca Cola", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Coca Cola", 2.25, 250)
    producto18 = Producto("Pepsi", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Pepsi", 1.85, 250)
    producto19 = Producto("Jugo de Naranja", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Jugo de Naranja", 3.00, 250)
    producto20 = Producto("Ponche de fruta","Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Ponche de fruta", 1.75, 250)
    producto21 = Producto("Raptor", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Raptor", 1.00, 250)
    producto22 = Producto("Monster", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Monster", 2.10, 250)
    producto23 = Producto("AMP", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "AMP", 1.00, 250 )
    producto24 = Producto("HiEnergy", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "HiEnergy", 1.00, 250 )
    producto25 = Producto("VOLT", "Proveedor3", datetime.date(2023, 5, 20), datetime.date(2023, 5, 9), "Ponche de fruta", 2.00, 250 )
    
    categoria1.productos.append(producto1)
    categoria1.productos.append(producto2)
    categoria1.productos.append(producto3)
    categoria1.productos.append(producto4)
    categoria1.productos.append(producto5)
    categoria1.productos.append(producto6)
    categoria1.productos.append(producto7)
    categoria1.productos.append(producto8)
    categoria1.productos.append(producto9)
    categoria1.productos.append(producto10)
    categoria2.productos.append(producto11)
    categoria2.productos.append(producto12)
    categoria2.productos.append(producto13)
    categoria2.productos.append(producto14)
    categoria2.productos.append(producto15)
    categoria3.productos.append(producto16)
    categoria3.productos.append(producto17)
    categoria3.productos.append(producto18)
    categoria3.productos.append(producto19)
    categoria3.productos.append(producto20)
    categoria4.productos.append(producto21)
    categoria4.productos.append(producto22)
    categoria4.productos.append(producto23)
    categoria4.productos.append(producto24)
    categoria4.productos.append(producto25)
    
    # Crear usuarios
    usuario1 = Usuario(1230, "Juan", 30, "Empleado")
    usuario2 = Usuario(2450, "Ana", 25, "Gerente")
    usuario3 = Usuario(3560, "Pedro", 40, "Supervisor")
    usuario4 = Usuario(4670, "Maria", 28, "Empleado")

    supermercado.agregar_usuario(usuario1)
    supermercado.agregar_usuario(usuario2)
    supermercado.agregar_usuario(usuario3)
    supermercado.agregar_usuario(usuario4)

    while True:
        print("\n¡BIENVENIDO AL SISTEMA DE NUESTRA TIENDA!")
        usuario_id = int(input("\nIngrese su ID de usuario (0 para salir): "))
        if usuario_id == 0:
            break

        supermercado.realizar_venta(usuario_id)

if __name__ == "__main__":
    main()