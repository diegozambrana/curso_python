l = [1, 2, 3, 4, 5, 'hola', 'Chau', True, [0, -1]]

for n in l:
    print(n)

for n in range(0, 5):
    print(n)



diccionario = {
    'telf': 45637821,
    'nombre': 'Diego',
    'email': 'diego@mail.com',
    'sexo': 'M',
    'lista': [
        'ir al mercado ',
        'comprar pan',
    ]
}

print(diccionario['lista'])



estudiantes = [
    {'nombre': 'Juan', 'nota': 51, 'materia': 'quimica', 'sexo': 'M'},
    {'nombre': 'Pedro', 'nota': 90, 'materia': 'quimica', 'sexo': 'M'},
    {'nombre': 'Alberto', 'nota': 49, 'materia': 'quimica', 'sexo': 'M'},
    {'nombre': 'Pepe', 'nota': 0, 'materia': 'quimica', 'sexo': 'M'},
    {'nombre': 'Maria', 'nota': 51, 'materia': 'quimica', 'sexo': 'F'},
    {'nombre': 'Marta', 'nota': 30, 'materia': 'quimica', 'sexo': 'F'},
    {'nombre': 'Ana', 'nota': 49, 'materia': 'quimica', 'sexo': 'F'},
    {'nombre': 'Juana', 'nota': 23, 'materia': 'quimica', 'sexo': 'F'},
]

total = 0
total_m = 0
total_f = 0
c_m = 0
c_f = 0

for estudiante in estudiantes:
    total = total + estudiante['nota']
    if(estudiante['sexo'] == 'M'):
        total_m = total_m + estudiante['nota']
        c_m = c_m + 1
    else:
        total_f = total_f + estudiante['nota']
        c_f = c_f + 1

print('promedio total: {}'.format(total/len(estudiantes)))
print('promedio total Hombres: {}'.format(total_m/c_m))
print('promedio total Mujeres: {}'.format(total_f/c_f))

# print(help(range))
print(list(range(0, 100, 10)))


palabra1 = input('ingrese la primera palabra: ')
palabra2 = input('ingrese la segunda palabra: ')

if(palabra1.lower() < palabra2.lower()):
    print(f'{palabra2} es mayor que {palabra1}')
elif(palabra1.lower() > palabra2.lower()):
    print(f'{palabra1} es mayor que {palabra2}')
else:
    print('ambas palabras son iguales')

print("hola como estas".capitalize())
print("hola como estas".upper())
print("Hola como Estas".lower())

texto = 'texto fuera mas largo'
print(help(str.find))
print(texto[texto.find('fue'): texto.find('mas') + 3])
print(texto.find('a', 14, 16))