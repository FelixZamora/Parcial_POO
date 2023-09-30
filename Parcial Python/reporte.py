from registro import *

class Reporte:

    def __init__(self):
        self.__informacionIntegrante = []

    def setUsuario(self, usuario: Registro):
        self.__informacionIntegrante.append(usuario)

    def getVehiculosIngresados(self):
        tiposTransporte = [["Bicicleta", 0], ["Moto", 0], ["Vehiculo", 0]]
        
        for integrante in self.__informacionIntegrante:
            tipoVehiculo = []
            tipoVehiculo.append(integrante.getRegistrarIngreso()) 

            if (str(tipoVehiculo[0][5]) == tiposTransporte[0][0]):
                tiposTransporte[0][1] += 1
                continue
            if (str(tipoVehiculo[0][5]) == tiposTransporte[1][0]):
                tiposTransporte[1][1] += 1
                continue
            if ((str(tipoVehiculo[0][5])) == tiposTransporte[2][0]):
                tiposTransporte[2][1] += 1
                continue

        cantidadTransporte = "\nCuantos medios de transporte ingresaron: \n" + str(tiposTransporte[0][0]) + ": " + str(tiposTransporte[0][1]) + "\n" + str(tiposTransporte[1][0]) + ": " + str(tiposTransporte[1][1]) + "\n" + str(tiposTransporte[2][0]) + ": " + str(tiposTransporte[2][1]) 
        return cantidadTransporte

    def getIntegranteMasIngresos(self):

        listaIntegrantes = []

        for i in self.__informacionIntegrante:
            datos = i.getRegistrarIngreso()
            listaIntegrantes.append(datos[1])
        
        frecuencia = {}

        for elemento in listaIntegrantes:
            if elemento in frecuencia:
                frecuencia[elemento] += 1
            else:
                frecuencia[elemento] = 1

        elemento_mas_comun = None
        max_frecuencia = 0

        for elemento, freq in frecuencia.items():
            if freq > max_frecuencia:
                max_frecuencia = freq
                elemento_mas_comun = elemento

        if elemento_mas_comun is not None:
            print(f"\nLa persona con el numero de identificacion {elemento_mas_comun} ingreso {max_frecuencia} veces en el parqueadero.")
        else:
            print("La lista está vacía.")

    def getTotalPagosDia(self):
        listaPagos = 0

        for x in self.__informacionIntegrante:
            datos = x.getRegistrarSalida()
            listaPagos += (datos[8])
        
        print ("\nEl total de pago realizados fueron: " , listaPagos)

    def getTotalPagosMes(self):
        listaPagos = 0

        for x in self.__informacionIntegrante:
            datos = x.getRegistrarSalida()
            listaPagos += (datos[8])
        
        print ("\nEl total de pago realizados fueron: " , listaPagos)