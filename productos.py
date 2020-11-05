from prettytable import PrettyTable
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)


def getAllProductos():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.productos;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        table = PrettyTable()
        table.field_names = [
            "idProductos",
            "nombre",
            "precio",
            "dimensiones",
            "materiales",
            "coloresDisponibles",
            "descripcion",
            "garantia",
            "idClaseProductos",
        ]
        for producto in result:
            table.add_row(
                [
                    producto["idProductos"],
                    producto["nombre"],
                    producto["precio"],
                    producto["dimensiones"],
                    producto["materiales"],
                    producto["coloresDisponibles"],
                    producto["descripcion"],
                    producto["garantia"],
                    producto["idClaseProductos"],
                ]
            )
        print(table)


def addProductos():
    print("Añadirás un nuevo producto")
    name = input("Nombre: ")
    precio = input("Precio: ")
    dimensiones = input("Dimensiones: ")
    materiales = input("Materiales: ")
    coloresDisponibles = input("Colores disponibles: ")
    descripcion = input("Descripción: ")
    garantia = input("Garantía: ")
    idClaseProductos = input("IdClaseProductos: ")

    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.productos (nombre, precio, dimensiones, materiales, coloresDisponibles, descripcion, garantia, idClaseProductos) values ('{name}','{precio}','{dimensiones}','{materiales}','{coloresDisponibles}','{descripcion}','{garantia}','{idClaseProductos}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllProductos()


def deleteProducto():
    result = []
    print("Borrarás un registro de la tabla productos")
    getAllProductos()
    idDel = int(input("Id del producto a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select idProductos, nombre, precio, descripcion from ikea.productos where idProductos = {idDel}; "
            indicacion = f"delete from ikea.productos where idProductos = {idDel};"
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            datosReg = (
                "IdProducto: "
                + str(registro["idProductos"])
                + ". Nombre: "
                + registro["nombre"]
                + ". Precio:  "
                + str(registro["precio"])
                + ". Descripción: "
                + registro["descripcion"]
            )
            print("Producto: " + datosReg)
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print("Se ha borrado definitivamente el registro: " + datosReg)
                getAllProductos()

            else:
                print("No se ha eliminado ningún registro de la tabla Productos")
                getAllProductos()

    finally:
        pass


def updateProducto():
    print("Modificarás un registro de la tabla Productos")
    getAllProductos()
    IdUpdate = int(input("Id del producto a modificar: "))
    result = []

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.productos where idProductos = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            producto = str(registro["idProductos"])
            nombre = registro["nombre"]
            precio = registro["precio"]
            dimensiones = registro["dimensiones"]
            materiales = registro["materiales"]
            coloresDisponibles = registro["coloresDisponibles"]
            descripcion = registro["descripcion"]
            garantia = registro["garantia"]
            idClaseProductos = registro["idClaseProductos"]
            datosReg = (
                "IdProducto: "
                + str(registro["idProductos"])
                + ". Nombre: "
                + nombre
                + ". Precio: $"
                + str(precio)
                + ". Dimensiones: "
                + dimensiones
                + ". Materiales: "
                + materiales
                + ". Colores disponibles: "
                + coloresDisponibles
                + ". Descripción: "
                + descripcion
                + ". Garantía: "
                + garantia
                + ". IdClaseProducto: "
                + str(idClaseProductos)
            )
            print(datosReg)

            option = int(input("Actualizar nombre? 1-Si, 0-No"))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre

            option = int(input("Actualizar precio? 1-Si, 0-No"))
            if option == 1:
                print("Precio actual: $" + precio)
                NuevoPrecio = input("Nuevo Precio: ")
                precio = NuevoPrecio

            else:
                precio = precio

            option = int(input("Actualizar dimensiones? 1-Si, 0-No"))
            if option == 1:
                print("Dimensiones actuales: " + dimensiones)
                NuevasDimensiones = input("Nuevas dimensiones: ")
                dimensiones = NuevasDimensiones

            else:
                dimensiones = dimensiones

            option = int(input("Actualizar materiales? 1-Si, 0-No"))
            if option == 1:
                print("Materiales actuales: " + materiales)
                NuevosMateriales = input("Nuevos Materiales: ")
                materiales = NuevosMateriales

            else:
                materiales = materiales

            option = int(input("Actualizar colores disponibles? 1-Si, 0-No"))
            if option == 1:
                print("Colores disponibles actuales: " + coloresDisponibles)
                NuevosColores = input("Nuevos colores disponibles: ")
                coloresDisponibles = NuevosColores

            else:
                coloresDisponibles = coloresDisponibles

            option = int(input("Actualizar descripción? 1-Si, 0-No"))
            if option == 1:
                print("Descripción actual: " + descripcion)
                NuevaDescripcion = input("Nueva descripción: ")
                descripcion = NuevaDescripcion

            else:
                descripcion = descripcion

            option = int(input("Actualizar garantía? 1-Si, 0-No"))
            if option == 1:
                print("Garantía actual: " + garantia)
                NuevaGarantia = input("Nueva garantía: ")
                garantia = NuevaGarantia

            else:
                garantia = garantia

            option = int(input("Actualizar Id clases de productos? 1-Si, 0-No"))
            if option == 1:
                print("IdClaseProducto actual: " + idClaseProductos)
                NuevoIdClaseProductos = input("Nuevo IdClaseProductos: ")
                idClaseProductos = NuevoIdClaseProductos

            else:
                idClaseProductos = idClaseProductos

            indicacion = f"UPDATE ikea.productos SET idProductos = '{producto}', nombre = '{nombre}', precio = '{precio}', dimensiones = '{dimensiones}', materiales = '{materiales}', coloresDisponibles = '{coloresDisponibles}', descripcion = '{descripcion}', garantia = '{garantia}', idClaseProductos = '{idClaseProductos}' where idProductos = '{producto}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllProductos()

    finally:
        pass
