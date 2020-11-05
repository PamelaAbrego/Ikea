from prettytable import PrettyTable
import pymysql

# Conexión a Servidor
connection = pymysql.connect(
    host="localhost",
    user="root",
    passwd="12345",
    db="ikea",
    cursorclass=pymysql.cursors.DictCursor,
)

# Tabla Categorías de Productos
# Obtener todas las categorías de productos


def getAllCategorias():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.categoriasproductos;"
            cursor.execute(sql)
            result = cursor.fetchall()

    finally:
        table = PrettyTable()
        table.field_names = ["idCategoriasProductos", "nombre"]
        for categoria in result:
            table.add_row([categoria["idCategoriasProductos"], categoria["nombre"]])
        print(table)


# Agregar un nueva categoría


def addNewCategoria():
    print("Añadirás una nueva categoría a la tabla Categorías de Productos")
    nombre = input("Nombre Categoría: ")

    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.categoriasproductos (nombre) values ('{nombre}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllCategorias()


# Borrar un País


def deleteCategoria():
    result = []
    print("Borrarás una categoría de la tabla Categorías de Productos")
    getAllCategorias()
    idDel = int(input("Id de la categoría a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.categoriasproductos where idCategoriasProductos = {idDel}; "
            indicacion = f"delete from ikea.categoriasproductos where idCategoriasProductos = {idDel}; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            datosReg = (
                "IdCategoriasProductos: "
                + str(registro["idCategoriasProductos"])
                + ". Nombre: "
                + registro["nombre"]
            )
            print(datosReg)
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print(
                    "Se ha borrado definitivamente el registro de la tabla Categorías de Productos: "
                    + datosReg
                )
                getAllCategorias()

            else:
                print(
                    "No se ha eliminado ningún registro de la tabla Categorías de Productos"
                )
                getAllCategorias()

    finally:
        pass


# Actualizar un País


def updateCategoria():
    print("Modificarás un registro de la tabla Categorías de Productos")
    getAllCategorias()
    IdUpdate = int(input("Id de la categoría a modificar: "))
    result = []

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.categoriasproductos where idCategoriasProductos = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            categoria = str(registro["idCategoriasProductos"])
            nombre = registro["nombre"]

            datosReg = "IdCategoria: " + categoria + ". Nombre: " + nombre
            print(datosReg)

            option = int(input("Actualizar nombre? 1-Si, 0-No"))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre

            indicacion = f"UPDATE ikea.categoriasproductos SET idCategoriasProductos = '{categoria}', nombre = '{nombre}' where idCategoriasProductos = '{categoria}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllCategorias()

    finally:
        pass


# Tabla clase de productos

# Obtener todas las clases de productos


def getAllClases():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT claseproductos.idClaseProductos, claseproductos.nombre, categoriasproductos.idCategoriasProductos, categoriasproductos.nombre as nombreCategoriaProducto FROM ikea.claseproductos inner join ikea.categoriasproductos on claseproductos.idCategoriasProductos= categoriasproductos.idCategoriasProductos;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        table = PrettyTable()
        table.field_names = [
            "idClaseProductos",
            "nombre",
            "idCategoriasProductos",
            "nombreCategoriaProducto",
        ]
        for clase in result:
            table.add_row(
                [
                    clase["idClaseProductos"],
                    clase["nombre"],
                    clase["idCategoriasProductos"],
                    clase["nombreCategoriaProducto"],
                ]
            )
        print(table)


# Ingresar una nueva clase


def addNewClase():
    print("Añadirás una nueva clase a la tabla Clase de Productos")
    nombre = input("Nombre Clase: ")
    getAllCategorias()
    categoria = str(input("Id de la categoría: "))

    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.claseproductos (nombre, idCategoriasProductos) values ('{nombre}', '{categoria}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllClases()


# Borrar una clase


def deleteClase():
    result = []
    print("Borrarás un registro de la tabla Clase de Productos")
    getAllClases()
    idDel = int(input("Id de la clase a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = (
                f"select * from ikea.claseproductos where idClaseProductos = {idDel}; "
            )
            indicacion = (
                f"delete from ikea.claseproductos where idClaseProductos = {idDel};"
            )
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            datosReg = (
                "IdClaseProductos: "
                + str(registro["idClaseProductos"])
                + ". Nombre: "
                + registro["nombre"]
                + ".IdCategoriaProductos: "
                + str(registro["idCategoriasProductos"])
            )
            print(datosReg)
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print("Se ha borrado definitivamente el registro: " + datosReg)
                getAllClases()

            else:
                print(
                    "No se ha eliminado ningún registro de la tabla Clases de Productos"
                )
                getAllClases()

    finally:
        pass


# Actualizar una ciudad


def updateClase():
    print("Modificarás un registro de la tabla Clases de Productos")
    getAllClases()
    IdUpdate = int(input("Id de la clase a modificar: "))
    result = []

    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.claseproductos where idClaseProductos = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            clase = str(registro["idClaseProductos"])
            nombre = registro["nombre"]
            categoria = str(registro["idCategoriasProductos"])

            print(
                "IdClaseProductos: "
                + clase
                + " Nombre: "
                + nombre
                + " IdCategoriasProductos: "
                + categoria
            )

            option = int(input("Actualizar nombre? 1-Si, 0-No"))
            if option == 1:
                print("Nombre actual: " + nombre)
                NuevoNombre = input("Nuevo nombre: ")
                nombre = NuevoNombre

            else:
                nombre = nombre

            option = int(input("Actualizar categoría? 1-Si, 0-No"))
            if option == 1:
                print("Categoría actual: " + pais)
                getAllCategorias()
                NuevaCategoria = int(input("Nueva Categoría: "))
                categoria = NuevaCategoria

            else:
                categoria = categoria

            indicacion = f"UPDATE ikea.claseproductos SET idClaseProductos = '{clase}', nombre = '{nombre}', idCategoriasProductos = '{categoria}' where idClaseProductos = '{clase}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllClases()

    finally:
        pass
