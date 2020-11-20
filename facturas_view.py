from prettytable import PrettyTable
from bdFacturas import (
    connection,
    getFacturaBD,
    insertFacturasBD,
    searchFacturasById,
    updateFacturasBD,
    deleteFacturasBD,
)
from usuarios_view import tablaUsuarios


class tablaFacturas:
    def __init__(self):
        self.getAllFacturas()

    def getAllFacturas(self):
        result = getFacturaBD()

        table = PrettyTable()
        table.field_names = [
            "Id",
            "IdUsuario",
            "NombreUsuario",
            "Tipo de pago",
            "IdSucursal",
            "Sucursal",
            "Fecha",
            "Hora",
            "IdCarrito",
        ]

        for factura in result:
            table.add_row(
                [
                    factura["idFacturas"],
                    factura["idUsuarios"],
                    factura["nombreUsuario"],
                    factura["tipoDePago"],
                    factura["idSucursales"],
                    factura["sucursal"],
                    factura["fecha"],
                    factura["hora"],
                    factura["idCarritos"],
                ]
            )
        print(table)
        table.clear()

    def addNewFactura(self):
        print("Se está añadiendo un nueva Factura:")
        print("--Tabla Usuarios--")
        tablaUsuarios()
        idUsuarios = int(input("idUsuario: "))
        tipoDePago = input("tipo de pago: ")
        idSucursales = int(input("Id Sucursal: "))
        fecha = input("Fecha: ")
        hora = input("Hora: ")
        idCarrito = int(input("Id Carrito: "))

        insertFacturasBD(idUsuarios, tipoDePago, idSucursales, fecha, hora, idCarrito)
        self.getAllFacturas()

    def updateFactura(self):
        print("Se está actualizando la información de una Factura : ")
        self.getAllFacturas()
        id = int(input("Id de la factura a actualizar: "))
        factura = searchFacturasById(id)

        option = int(input("¿Desea actualizar el IdUsuario? 0.No, 1.Sí: "))
        if option == 1:
            print("--Tabla Usuarios--")
            tablaUsuarios()
            print(f"IdUsuario anterior: {factura['idUsuarios']}")
            idUsuarios = input("Nuevo idUsuario: ")

        else:
            idUsuarios = factura["idUsuarios"]

        option = int(input("¿Desea actualizar el tipo de pago? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Tipo de pago anteriores: {factura['tipoDePago']}")
            tipoDePago = input("Nuevao tipo de pago: ")

        else:
            tipoDePago = factura["tipoDePago"]

        option = int(input("¿Desea actualizar el idSucursal? 0.No, 1.Sí: "))
        if option == 1:
            # Anclar tabla sucursales
            print(f"IdSucursal anteriores: {factura['IdSucursales']}")
            idSucursales = input("Nuevo ID sucursal: ")

        else:
            idSucursales = factura["idSucursales"]

        option = int(input("¿Desea actualizar la fecha? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Fecha anterior: {factura['fecha']}")
            fecha = input("Nueva fecha: ")

        else:
            fecha = factura["fecha"]

        option = int(input("¿Desea actualizar la hora? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Hora anterior: {factura['hora']}")
            hora = input("Nueva hora: ")

        else:
            hora = factura["hora"]

        option = int(input("¿Desea actualizar el Id del carrito? 0.No, 1.Sí: "))
        if option == 1:
            print(f"Id Carrito anterior: {factura['idCarritos']}")
            idCarrito = input("Nuevo IdCarrito: ")

        else:
            idCarrito = factura["idCarritos"]

        updateFacturasBD(
            idUsuarios, tipoDePago, idSucursales, fecha, hora, idCarrito, id
        )
        self.getAllFacturas()

    def deleteFactura(self):
        print("Se está eliminando una Factura: ")
        self.getAllFacturas()
        id = int(input("Id de la factura a eliminar: "))
        deleteFacturasBD(id)
        self.getAllFacturas()
