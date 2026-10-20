"""
PROBLEMA:
Calcular el importe de un viaje en taxi según los kilómetros recorridos.

ENTRADAS:
kilometros: número real, en km, mayor o igual a 0.

SALIDAS:
Importe final en pesos, mostrado con dos decimales.

REGLAS Y SUPUESTOS:
- Banderazo fijo de $35.
- Costo de $9 por kilómetro.
- Si los kilómetros son mayores que 20, aplicar 10% de descuento.
- Si son exactamente 20 km, no aplicar descuento.
- Mostrar el importe con dos decimales.

ALGORITMO:
1. Leer los kilómetros.
2. Calcular 35 + 9 * kilometros.
3. Si kilometros > 20, multiplicar el importe por 0.90.
4. Mostrar el importe final.

CASOS DE PRUEBA:
5 km -> $80.00
20 km -> $215.00
21 km -> $201.60
30 km -> $274.50

RESTRICCIONES PARA EL AGENTE:
- Usar únicamente la biblioteca tabulate.
- No agregar bibliotecas adicionales.
- Implementar las funciones del contrato.

CONTRATO DE FUNCIONES:
leerKilometros(): lee y retorna los kilómetros.
calcularImporte(kilometros): retorna el importe final.
mostrarImporte(importe): muestra el resultado en una tabla.
"""

from tabulate import tabulate

def leerKilometros():
    return float(input("Ingrese los kilómetros recorridos: "))

def calcularImporte(kilometros):
    importe = 35 + 9 * kilometros
    if kilometros > 20:
        importe *= 0.90
    return round(importe, 2)

def mostrarImporte(importe):
    tabla = [["Importe", f"${importe:.2f}"]]
    print(tabulate(tabla, headers="firstrow", tablefmt="grid"))

