def resultado(nota, estudiante, materia):
    try:
        nota = int(nota)
    except:
        return 'El valor de Nota no es un valor numerico'

    if(estudiante == ''):
        return 'Debe ingresar el nombre del estudiante'

    if(nota < 0 or nota > 100):
        return 'Fuera de rango'
    else:
        if (nota >= 51):
            return f'el estudiante {estudiante} a Aprobado con {nota} la materia de {materia}'
        elif (nota == 0):
            return f'el estudiante {estudiante} a Abandonado la materia de {materia}'
        else:
            return f'el estudiante {estudiante} a Reprobado con {nota} la materia de {materia}'


nota = input('ingrese la nota: ')
nombre = input('Ingrese el nombre: ')
materia = input('Ingrese el nombre de la materia: ')

print(resultado(nota, nombre, materia))


def costo_a_pagar(horas, minutos, precio_por_hora):
    return (horas + minutos/60) * precio_por_hora


horas = int(input('ingrese las horas: '))
minutos = int(input('ingrese los minutos: '))
precio_por_hora = float(input('ingrese el precio por hora: '))

total = costo_a_pagar(horas, minutos, precio_por_hora)
print('el costo a pagar por {}:{} trabajadas es {} Bs.'.format(horas, minutos, total))