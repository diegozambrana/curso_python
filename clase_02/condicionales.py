# Condicionales

#Expresiones Booleanas

p = 1
q = 2
print('p == q : {}'.format(p == q))
print('p != q : {}'.format(p != q))
print('p > q : {}'.format(p > q))
print('p < q : {}'.format(p < q))
print('p >= q : {}'.format(p >= q))
print('p <= q : {}'.format(p <= q))
print('p is q : {}'.format(p is q))
print('p is not q : {}'.format(p is not q))

# Operadores Lógicos

x = 1
y = 3
z = x > 3 and y > x
print('x > 3 and y > x :', z)
z = x > 3 or y > x
print('x > 3 or y > x :', z)
z = not (x > 3 or y > x)
print('not (x > 3 or y > x) :', z)

print('texto' and True)

# valor None
valor_none = None
print(valor_none is None)

# if
# ejemplo 1
x = 5
if x > 1:
    print(x, 'es mayor a', 1)

# ejemplo 2
x = 5
if x % 2 == 0:
    print(x, 'es par')
else:
    print(x, 'es impar')

# ejemplo 3

x = 12
y = 11

if x > y:
    print(x, 'es mayor a', y)
elif x < y:
    print(x, 'es menor a', y)
else:
    print(x, 'es igual a', y)

# asignación condicional
x = 10
y = 11
z = x if x > y else y
print('z es {}'.format(z))

# try and except
try:
    x = 2 + 3
    y = '6'
    z = x // y
except:
    print('los valores de x o y no son correctos')

# ejemplo 2
try:
    edad = input('Ingrese su edad:\n> ')
    horas = int(edad) * 365 * 24
    print('usted tiene aproximadamente {} horas de vida'.format(horas))
except:
    print('ingrese un valor numérico')