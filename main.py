import json
import csv

def cargar_json():
    with open ("productos.json", "r") as archivo:
        productos = json.load(archivo)
    return productos

def guardar_json(productos):
    with open("productos.json","w") as archivo:
        json.dump(productos,archivo)

def listar_produ(productos):
    if len(productos) == 0:
        print("No hay productos!!!")
        return

    for producto in productos:
        print(f"id: {producto['id']}")
        print(f"nombre:{producto['nombre']}")
        print(f"categoria {producto['categoria']}")
        print(f"precio{producto['precio']}")
        print(f"stock{producto['stock']}")

def agregar_produ(productos):

    id = int(input("ingrese id del producto:"))
    nombre = input("ingrese nombre del producto:")
    categoria = input("ingrese categoria del producto:")
    precio = int(input("ingrese precio del producto:"))
    stock = int(input("ingrese el stock del producto"))

    producto_nuevo = {
        "id" : id,
        "nombre" : nombre,
        "categoria" : categoria,
        "precio" : precio,
        "stock" : stock
        }

    productos.append(producto_nuevo)
    print("Producto Agregado")

def buscar_producto (productos):

    nombre = input("ingrese el nombre: ")
    encontrado = False

    for producto in productos:
        if producto["nombre"] == nombre:
            print(producto)
            encontrado = True
    if not encontrado:
        print ("No se encontro el producto!")

def modificar_stock(productos):
    id_buscar = int(input("ingrese el ID del producto: "))

    for producto in productos:
        if producto ["id"] == id_buscar:
            nuevo_stock = int(input("nuevo stock: "))
            producto["stock"] = nuevo_stock

            print ("Stock actualizado")
            return

    print("Producto no encontrado!!!")

def eliminar_producto(productos):
    id_buscar = int(input("ingrese id del producto:"))

    for producto in productos:
        if producto["id"] == id_buscar:
            productos.remove(producto)

            print("Producto Eliminado!!!")
            return
    print("Producto no encontrado")

def mostar_categoria (productos):
    categoria = input("ingrese la categoria del producto:")
    encontrado = False

    for producto in productos:
        if producto ["categoria"] == categoria:
            print(f"ID:{producto['id']}, nombre:{producto['nombre']}, categoria:{producto['categoria']}, precio:{producto['precio']}, stock: {producto['stock']}")
            encontrado = True
    if not encontrado:
        print("No se encontro el producto!!!")

def mostrar_estadisticas (productos):
    if len(productos) == 0:
        print("No hay productos !")
        return

    total_stock = 0

    mas_caro = productos[0] 
    mas_barato = productos [0]

    for producto in productos:
        total_stock += producto["stock"]

        if producto['precio'] < mas_barato['precio']:
            mas_barato = producto

        if producto['precio'] > mas_caro ['precio']:
            mas_caro = producto

    print(f"Cantidad de productos: {len(productos)}")
    print(f"stock total: {total_stock}")
    print(F"producto mas caro {mas_caro['precio']}")
    print(f"producto mas barato {mas_barato['precio']}")

def exportar_csv(productos):
    with open("reporte_productos.csv", "w") as archivo:
        archivo.write ("id, nombre, categoria, precio, stock \n") 

        for producto in productos:
            linea = f"{producto['id']},{producto['nombre']},{producto['categoria']},{producto['precio']},{producto['stock']}\n"
            archivo.write(linea)
        print("CSV generado correctamente")


productos = cargar_json()

while True:
    print("\n===== SUPERMERCADO =====")
    print("1. listar productos")
    print("2. agregar productos")
    print("3. buscar producto")
    print("4. modificar stock")
    print("5. eliminar producto")
    print("6. mostar por categoria")
    print("7. mostrar estadisticas")
    print("8. exportar csv")
    print("9. guardar y salir")

    opcion = (input("ingrese una opcion:"))

    if opcion == "1":
        listar_produ(productos)

    elif opcion == "2":
        agregar_produ(productos)

    elif opcion == "3":
        buscar_producto(productos)

    elif opcion == "4":
        modificar_stock(productos)

    elif opcion == "5":
        eliminar_producto(productos)

    elif opcion == "6":
        mostar_categoria(productos)

    elif opcion == "7":
        mostrar_estadisticas(productos)

    elif opcion == "8":
        exportar_csv(productos)

    elif opcion == "9":
        guardar_json(productos)
        print("Datos guardados")
        break
    else:
        print("OPCION INVALIDA!!!")
