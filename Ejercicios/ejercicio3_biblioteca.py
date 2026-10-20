"""
PROBLEMA:
Calcular la multa por retraso en la devolución de un libro.

ENTRADAS:
dias: número entero de días, mayor o igual a 0.

SALIDAS:
Multa en pesos, con dos decimales.

REGLAS Y SUPUESTOS:
- Los primeros 10 días cuestan $5 por día.
- Cada día posterior al décimo cuesta $10.
- La multa máxima es de $200.
- Cero días de retraso generan una multa de $0.
- Se limita la multa a $200.

ALGORITMO:
1. Leer los días de retraso.
2. Calcular los días cobrados a $5, con máximo de 10.
3. Calcular los días restantes a $10.
4. Sumar los importes.
5. Limitar la multa a $200.
6. Mostrar el resultado.

CASOS DE PRUEBA:
0 días -> $0.
10 días -> $50.
11 días -> $60.
25 días -> $200.
40 días -> $200.

RESTRICCIONES PARA EL AGENTE:
- La única biblioteca permitida es tabulate.
- No agregar bibliotecas adicionales.

CONTRATO DE FUNCIONES:
leerDias(): lee y retorna los días de retraso.
calcularMulta(dias): retorna la multa final.
mostrarMulta(multa): muestra la multa en una tabla.
"""
from tabulate import tabulate


def leerDias():
    dias = int(input("Ingrese los días de retraso: "))
    return dias


def calcularMulta(dias):
    dias_iniciales = min(dias, 10)
    dias_adicionales = max(dias - 10, 0)

    multa = dias_iniciales * 5 + dias_adicionales * 10

    if multa > 200:
        multa = 200

    return multa


def mostrarMulta(multa):
    filas = [["Multa de biblioteca", f"${multa:.2f}"]]
    print(tabulate(filas, headers=["Concepto", "Importe"],
                   tablefmt="grid"))