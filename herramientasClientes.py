import pymysql
from prettytable import PrettyTable

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def BuscarProducto():
    while True:
        print("¿Cómo deseas realizar tu búsqueda?")
        print("1. Escribir lo que buscas")
        print("2. Directorio de categorías")
        print(" ")
        opcion = int(input("Opción: "))

        if opcion == 1:
            producto = input("¿Qué estás buscando?")
            try:
                with connection.cursor() as cursor:
                    sql = f"""select ikea.categoriasproductos.nombre, ikea.claseproductos.nombre,
                        ikea.productos.idProductos, ikea.productos.nombre, ikea.productos.precio,
                        ikea.productos.dimensiones, ikea.productos.materiales, ikea.productos.coloresDisponibles,
                        ikea.productos.descripcion, ikea.productos.garantia from ikea.categoriasproductos inner join
                        ikea.claseproductos on ikea.claseproductos.idCategoriasProductos = ikea.categoriasproductos.idCategoriasProductos inner join
                        ikea.productos on ikea.productos.idClaseProductos = ikea.claseproductos.idClaseProductos where
                        ikea.categoriasproductos.nombre = '{producto}' or ikea.claseproductos.nombre = '{producto}' or
                        ikea.productos.nombre = '{producto}';"""
                    cursor.execute(sql)
                    result = cursor.fetchall()

            finally:
                table = PrettyTable()
                table.field_names = [
                    "Categoría",
                    "Clase",
                    "idProducto",
                    "Nombre producto",
                    "Precio",
                    "Dimensiones",
                    "Materiales",
                    "Colores disponibles",
                    "Descripción",
                    "Garantía",
                ]
                for product in result:
                    table.add_row(
                        [
                            product["nombre"],
                            product["claseproductos.nombre"],
                            product["idProductos"],
                            product["productos.nombre"],
                            product["precio"],
                            product["dimensiones"],
                            product["materiales"],
                            product["coloresDisponibles"],
                            product["descripcion"],
                            product["garantia"],
                        ]
                    )
                print(" ")
                print(" ")
                print(
                    "Estos son todos los productos que se han encontrado con tu busqueda: "
                    + str(producto)
                )
                print(table)
                print(" ")
                dec = int(input("Deseas seguir buscando productos? 1: Si, 0: No "))
                if dec == 1:
                    BuscarProducto()
                else:
                    break

        if opcion == 2:
            print("Estas son las CATEGORÍAS DE PRODUCTOS: ")
            listaCategorias = []
            listaClases = []
            intA = 1
            intC = 1
            try:
                with connection.cursor() as cursor:
                    sql = f"select ikea.categoriasproductos.nombre from ikea.categoriasproductos;"
                    Dict = {}
                    Dict2 = {}
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for category in result:
                        listaCategorias.append(category["nombre"])

                    for cat in listaCategorias:
                        print(str(intC) + "." + cat)
                        Dict.update({intC: cat})
                        intC = intC + 1

                    option = int(input("¿Qué categoría de producto deseas buscar?"))
                    categoria = Dict[option]

                    sql2 = f"""select ikea.claseproductos.nombre from ikea.claseproductos inner join
                        ikea.categoriasproductos on ikea.claseproductos.idCategoriasProductos = ikea.categoriasproductos.idCategoriasProductos
                        where ikea.categoriasproductos.nombre = '{categoria}';"""
                    cursor.execute(sql2)
                    result2 = cursor.fetchall()

                    for clase in result2:
                        listaClases.append(clase["nombre"])

                    print("Estas son las CLASES DE PRODUCTOS: ")

                    for cla in listaClases:
                        print(str(intA) + "." + cla)
                        Dict2.update({intA: cla})
                        intA = intA + 1

                    num = int(input("¿Qué clase de producto de deseas buscar?"))
                    clath = Dict2[num]

                    sql3 = f"""select ikea.productos.idProductos, ikea.productos.nombre, ikea.productos.precio,
                        ikea.productos.dimensiones, ikea.productos.materiales, ikea.productos.coloresDisponibles,
                        ikea.productos.descripcion, ikea.productos.garantia from ikea.productos inner join
                        ikea.claseproductos on ikea.productos.idClaseProductos = ikea.claseproductos.idClaseProductos
                        where ikea.claseproductos.nombre = '{clath}';"""
                    cursor.execute(sql3)
                    result3 = cursor.fetchall()

            finally:
                table2 = PrettyTable()
                table2.field_names = [
                    "idProdcto",
                    "Nombre Producto",
                    "Precio",
                    "Dimensiones",
                    "Materiales",
                    "Colores Disponibles",
                    "Descripción",
                    "Garantía",
                ]
                for product in result3:
                    table2.add_row(
                        [
                            product["idProductos"],
                            product["nombre"],
                            product["precio"],
                            product["dimensiones"],
                            product["materiales"],
                            product["coloresDisponibles"],
                            product["descripcion"],
                            product["garantia"],
                        ]
                    )
                print(" ")
                print("Estos son los resultados de tu búsqueda:")
                print(table2)

                dec = int(input("¿Deseas seguir buscando productos? 1 - Si, 0 - No "))
                if dec == 1:
                    BuscarProducto()
                else:
                    break
