"""
PROBLEMA:
Calcular la comisión, el bono y el total a pagar a un vendedor.

ENTRADAS:
ventas: número real en pesos, mayor o igual a 0.

SALIDAS:
Comisión, bono y total a pagar en pesos con dos decimales.

REGLAS Y SUPUESTOS:
- Menos de $10,000: comisión del 5%.
- Desde $10,000 inclusive: comisión del 8%.
- Más de $50,000: bono adicional de $1,000.
- Exactamente $50,000 no genera bono.
- Total a pagar = comisión + bono.

ALGORITMO:
1. Leer el importe de las ventas.
2. Calcular la comisión según el porcentaje correspondiente.
3. Calcular el bono según el importe de las ventas.
4. Sumar comisión y bono.
5. Mostrar los tres importes.

CASOS DE PRUEBA:
$5,000 -> comisión $250, bono $0, total $250.
$10,000 -> comisión $800, bono $0, total $800.
$50,000 -> comisión $4,000, bono $0, total $4,000.
$50,001 -> comisión $4,000.08, bono $1,000,
           total $5,000.08.

RESTRICCIONES PARA EL AGENTE:
- La única biblioteca permitida es tabulate.
- No agregar bibliotecas adicionales.

CONTRATO DE FUNCIONES:
leerVentas(): lee y retorna las ventas.
calcularComision(ventas): retorna la comisión.
calcularBono(ventas): retorna el bono.
mostrarPago(comision, bono): muestra comisión, bono y total.
"""
from tabulate import tabulate

def leerVentas():
    return float(input("Ingrese el importe de las ventas: "))

def calcularComision(ventas):
    if ventas < 10000:
        return round(ventas * 0.05, 2)
    else:
        return round(ventas * 0.08, 2)

def calcularBono(ventas):
    if ventas > 50000:
        return 1000
    else:
        return 0

def mostrarPago(comision, bono):
    total = comision + bono
    tabla = [
        ["Comisión", f"${comision:.2f}"],
        ["Bono", f"${bono:.2f}"],
        ["Total", f"${total:.2f}"]
    ]
    print(tabulate(tabla, headers="firstrow", tablefmt="grid"))

