print(1, 'hola')
print('hola' + ' mundo')
print('hola {}'.format('mundo'))
mundo = 'mundo!!'
print(f"hola {mundo}")


print(len('hola mundo'))
print(len([0, 2, 3]))
print(max('hola mundo'))
print(min('holaMundo'))

print(max([1, 2, 3, 4, 5, 6]))
print(min([-76, 1, 2, 3, 4, 5, 6]))
print(type(int('23')))
print(type('23'))
print(str(1234))
print(str(True))
print(float(1))

import math

print(math.sin(0.7))
print(math.cos(0.7))
print(math.tan(0.7))

print(math.sqrt(9))

import random

print(random.random())
print(random.randint(-100, 100))
print(random.choice(['A', 'B', 'C', 'D']))

def saludar(nombre):
    return f"Hola {nombre}, es un gusto conocerte!"

print(saludar('Diego'))


def resultado(nota, estudiante):
    if(nota >= 51):
        # 'el estudiante ' + estudiante + ' a abprobado con ' + nota
        return f'el estudiante {estudiante} a Aprobado con {nota}'
    elif(nota == 0):
        return f'el estudiante {estudiante} a Abandonado la materia'
    else:
        return f'el estudiante {estudiante} a Reprobado con {nota}'

print(resultado(1, 'Juan'))
print(resultado(0, 'Pedro'))
print(resultado(99, 'Jacob'))

res_alvaro = resultado(51, 'Alvaro')
print(res_alvaro)