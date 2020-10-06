print('suma 1 + 2 = {}'.format(1 + 2))
print('resta 4 - 2 = {}'.format(4 - 2))
print('multiplicación 3 * 2 = {}'.format(3 * 2))
# En python 2.0 la división te devolvía un entero, python 3.0 te devuelve un typo flotante
print('división 10 / 3 = {}'.format(10 / 3))
# Para obtener un entero se usa //
print('división 10 // 3 = {}'.format(10 // 3))
print('potencia 5 ** 3 = {}'.format(5 ** 3))

print('Módulo 5 % 3 = {}'.format(5 % 3))

# expreciones
# 13
# x
# x + 13
print((3 + 2) ** 3)

"""
Orden de las operaciones
python utiliza PEMDAS

1. Parentheses first: parentesis
2. Exponents: Potencias
3. Multiplication and Divisio: Multiplicación y División
4. Addition and Subtraction: Suma y Resta
"""

# (10 + 2) + 3 * 4 - ((2 ** 2) * (2 + 3))
# 12 + 12 - 2 ** 2 * 5
# 12 + 12 - 4 * 5
# 12 + 12 - 20
# 4

(10 + 2) + 3 * 4 - 2 ** 2 * (2 + 3)