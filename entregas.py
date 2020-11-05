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


# Obtener todos los registros de la tabla Entregas
def getAllEntregas():
    result = {}
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ikea.entregas;"
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        table = PrettyTable()
        table.field_names = ["idEntregas", "idFacturas", "fecha", "hora", "lugar"]
        for entrega in result:
            table.add_row(
                [
                    entrega["idEntregas"],
                    entrega["idFacturas"],
                    entrega["fecha"],
                    entrega["hora"],
                    entrega["lugar"],
                ]
            )
        print(table)


# Agregar una nueva entrega


def addNewEntrega():
    print("Añadirás una nueva entrega: ")
    idFactura = input("idFactura: ")
    fecha = input("fecha: ")
    hora = input("hora")
    lugar = input("lugar: ")

    try:
        with connection.cursor() as cursor:
            sql = f"insert into ikea.entregas (idFacturas, fecha, hora, lugar) values ('{idFactura}','{fecha}','{hora}','{lugar}');"
            cursor.execute(sql)
            connection.commit()

    finally:
        getAllEntregas()


# Borrar un registro de la tabla Entregas


def deleteEntrega():
    result = []
    print("Borrarás un registro de la tabla entregas")
    idDel = int(input("Id de la entrega a borrar: "))

    try:
        with connection.cursor() as cursor:
            sql = f"select idEntregas, idFacturas, fecha, hora, lugar from ikea.entregas where idEntregas = {idDel}; "
            indicacion = f"delete from ikea.entregas where idEntregas = {idDel};"
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            datosReg = (
                "IdEntrega: "
                + str(registro["idEntregas"])
                + ". IdFactura: "
                + str(registro["idFacturas"])
                + ". Fecha: "
                + str(registro["fecha"])
                + ". Hora: "
                + str(registro["hora"])
                + ". Lugar: "
                + registro["lugar"]
            )
            print("Entrega: " + datosReg)
            print("Borrarás definitivamente el registro anterior. Estás seguro?")
            opcion = int(input("Si(1), No(0). Escribe 1 o 0."))

            if opcion == 1:
                cursor.execute(indicacion)
                connection.commit()
                print("Se ha borrado definitivamente el registro: " + datosReg)
                getAllEntregas()

            else:
                print("No se ha eliminado ningun registro de la tabla entregas")
                getAllEntregas()

    finally:
        pass


# Modificar una entrega


def updateEntrega():
    print("Modificarás un registro de la tabla entregas")
    getAllEntregas()
    IdUpdate = int(input("Id de la entrega a modificar: "))
    result = []
    try:
        with connection.cursor() as cursor:
            sql = f"select * from ikea.entregas where idEntregas = '{IdUpdate}'; "
            cursor.execute(sql)
            result = cursor.fetchall()
            registro = result[0]
            entrega = str(registro["idEntregas"])
            idFactura = registro["idFacturas"]
            fecha = registro["fecha"]
            hora = registro["hora"]
            lugar = registro["lugar"]
            datosReg = (
                "IdEntregas: "
                + str(entrega)
                + ". IdFacturas:  "
                + str(idFactura)
                + ". Fecha: "
                + str(fecha)
                + ". Hora: "
                + str(hora)
                + ". Lugar: "
                + lugar
            )
            print(datosReg)

            option = int(input("Actualizar IdFactura? 1-Si, 0-No"))
            if option == 1:
                print("idFactura actual: " + str(idFactura))
                NewIdFactura = input("Nuevo idFactura: ")
                idFactura = NewIdFactura

            else:
                idFactura = idFactura

            option = int(input("Actualizar fecha? 1-Si, 0-No"))
            if option == 1:
                print("fecha actual: " + str(fecha))
                NewFecha = input("Nueva fecha: ")
                fecha = NewFecha

            else:
                fecha = fecha

            option = int(input("Actualizar hora? 1-Si, 0-No"))
            if option == 1:
                print("hora actual: " + str(hora))
                NewHora = input("Nueva hora: ")
                hora = NewHora

            else:
                hora = hora

            option = int(input("Actualizar lugar? 1-Si, 0-No"))
            if option == 1:
                print("lugar actual: " + lugar)
                NewLugar = input("Nuevo lugar: ")
                lugar = NewLugar

            else:
                lugar = lugar

            indicacion = f"UPDATE ikea.entregas SET idEntregas = '{entrega}', idFacturas = '{idFactura}', fecha = '{fecha}', hora = '{hora}', lugar = '{lugar}' where idEntregas = '{entrega}';"
            cursor.execute(indicacion)
            connection.commit()
            getAllEntregas()

    finally:
        pass
