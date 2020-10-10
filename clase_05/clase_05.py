# ejercicio 2
cadena1 = input('cadena1: ')
cadena2 = input('cadena2: ')

total = 0

while cadena1 in cadena2:
    total = total + 1
    cadena2 = cadena2[cadena2.find(cadena1) + len(cadena1): ]

if(total == 0):
    print('no esta')
else:
    print('total = {}'.format(total))

# Ejercicio 3
cadena = input('ingrese su cadena: ')
resultado = ''
vocales = 'aeiou'

for c in cadena:
    if c in vocales:
        resultado = resultado + str(vocales.find(c) + 1)
    else:
        resultado = resultado + c

print('resultado: {}'.format(resultado))


# funciones de cadenas 

texto = "     hola mundo      "
texto1 = "Hola Mundo"
print(texto.strip())
print(texto1.replace('a', '1').replace('o', '4').replace('u', '5'))
print(texto1.replace('Mundo', 'Bolivia'))
print(texto1.startswith('hola'))
print(texto1.endswith('do'))

texto2 = 'hola mundo como estas'
print(texto2.split())
print(len(texto2.split()))

# concatenar
text = 'Mundo'
numero = 2
decimal = 3.2

print("hola %s, numero: %d, decimal: %g" % (text, numero, decimal))
print(f"hola {text}, numero: {numero}, decimal: {decimal}")
print("hola {}, numero: {}, decimal: {}".format(text, numero, decimal))

# Ejercicio de Cadenas
# Al ingresar un texto, cuente el numero de palabras, y también que devuelva la palabra mas larga y la palabra mas corta.
cadena = input('ingrese texto: ')
palabra_larga = ''
palabra_corta = ''

for palabra in cadena.split():
    if len(palabra) > len(palabra_larga):
        palabra_larga = palabra
    if len(palabra) < len(palabra_corta) or palabra_corta == '' :
        palabra_corta = palabra

if palabra_larga == '':
    print('no ingreso ningun texto')
else:
    print(f'palabra larga: {palabra_larga}, palabra corta: {palabra_corta}, total palabras: {len(cadena.split())}')