class Registro:
    def __init__(self):
        self.__tiposTransporte = ""
        self.__tiposIntegrante = ""
        self.__fecha = ""
        self.__horaEntrada = ""
        self.__placa = ""
        self.__nombreIntegrante = ""
        self.__identificacionIntegrante = ""
        self.__horaSalida = ""
        self.__tarifa = ""

    def setRegistrarIngreso(self, nombreIntegrante, identificacionIntegrante,tiposIntegrante, fecha, horaEntrada, tiposTransporte, placa):
        self.__nombreIntegrante = nombreIntegrante
        self.__identificacionIntegrante = identificacionIntegrante
        self.__tiposIntegrante = tiposIntegrante
        self.__fecha = fecha
        self.__horaEntrada = horaEntrada
        self.__tiposTransporte = tiposTransporte
        self.__placa = placa
        

    def getRegistrarIngreso(self):
        datosIngreso = [self.__nombreIntegrante, self.__identificacionIntegrante, self.__tiposIntegrante, self.__fecha, self.__horaEntrada, self.__tiposTransporte, self.__placa]
        return(datosIngreso)

    def setRegistrarSalida(self, horaSalida, tarifa):
        self.__horaSalida = horaSalida
        self.__tarifa = tarifa
        

    def getRegistrarSalida(self):
        datosSalida = [self.__nombreIntegrante, self.__identificacionIntegrante, self.__tiposIntegrante, self.__fecha, self.__horaEntrada, self.__tiposTransporte, self.__placa]
        datosSalida.append(self.__horaSalida)
        datosSalida.append(self.__tarifa)
        return (datosSalida)
