from registro import *
from reporte import *

usuario1 = Registro()
usuario1.setRegistrarIngreso("Nelson Vargas", 11282451, "Estudiante", "28/09/2023", "10:12 PM", "Moto", "C5D15A")
usuario1.getRegistrarIngreso()
usuario1.setRegistrarSalida("12:12 PM", 25000)
usuario1.getRegistrarSalida()

usuario2 = Registro()
usuario2.setRegistrarIngreso("Miguel Pineda", 85956874, "Profesor", "29/09/2023", "10:55 PM", "Vehiculo", "LO85AE")
usuario2.getRegistrarIngreso()
usuario2.setRegistrarSalida("12:12 PM", 29000)
usuario2.getRegistrarSalida()

usuario3 = Registro()
usuario3.setRegistrarIngreso("Miguel Pineda", 85956874, "Profesor", "29/09/2023", "10:56 PM", "Vehiculo", "LO85AE")
usuario3.getRegistrarIngreso()
usuario3.setRegistrarSalida("12:13 PM", 21000)
usuario3.getRegistrarSalida()

usuarios = [usuario1, usuario2, usuario3]

reporteAdmin = Reporte()
reporteAdmin.setUsuario(usuario1)
reporteAdmin.setUsuario(usuario2)
reporteAdmin.setUsuario(usuario3)
print(reporteAdmin.getVehiculosIngresados())
reporteAdmin.getIntegranteMasIngresos()
reporteAdmin.getTotalPagosDia()

