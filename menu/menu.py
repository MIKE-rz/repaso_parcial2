from Ejercicios.ejercicio1_taxi import leerKilometros, calcularImporte, mostrarImporte
from Ejercicios.ejercicio2_comision import leerVentas, calcularComision, calcularBono, mostrarPago
from Ejercicios.ejercicio3_biblioteca import leerDias, calcularMulta, mostrarMulta

def mostrarMenu():
    print(" REPASO DEL EXAMEN ")
    print("1. Viaje en taxi")
    print("2. Comisión de ventas")
    print("3. Multa de biblioteca")
    print("0. Salir")


def ejecutarMenu():
    while True:
        mostrarMenu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            kilometros = leerKilometros()
            importe = calcularImporte(kilometros)
            mostrarImporte(importe)

        elif opcion == "2":
            ventas = leerVentas()
            comision = calcularComision(ventas)
            bono = calcularBono(ventas)
            mostrarPago(comision, bono)
        elif opcion == "3":
            dias = leerDias()
            multa = calcularMulta(dias)
            mostrarMulta(multa)
            
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")