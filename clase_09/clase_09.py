A = {1, 2, 3, 3, 3, 4}
B = set([4, 5, 6, 6, 6])

print(A)
print(list(B))

A.add(5)
print(A)

A.remove(5)
print(A)

A.discard(5)
print(A)

print(A.pop())
print(A)

A.clear()
print(A)


# Union
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)
print(A.union(B))
A.update(B)
print(A)

# Interseccion
print('- Interseccion')
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)
print(A.intersection(B))

A.intersection_update(B)
print(A)


# Diferencia
print('- Diferencia')
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)
print(B - A)
print(A.difference(B))

A.difference_update(B)
print(A)

# Diferencia Simetrica
print('- Diferencia Simetrica')
A = {4, 5, 1, 2, 3}
B = {4, 5, 6, 7, 8}
print(A ^ B)
print(A.symmetric_difference(B))
A.symmetric_difference_update(B)
print(A)



A = set('Manzana')
print(A)

print('a' in A)

B = {True, False, True}
print(all(B))
print(any(B))
# print(all([True, False, True]))

A = {4, 5}
B = {1, 2, 3}

print(A.isdisjoint(B))
print(B.isdisjoint(A))

A = {'hola', 'mundo'}
B = {'Chau', 'mundo'}
print(A | B)
print(len(A))

lista_A = [1, 2, 3]
lista_B = [3, 4, 5]

A = set(lista_A)
B = set(lista_B)

print(A.intersection(B))

# Ejercicio 3

lista_A = [ 2, 3, 4, 4, 5, 6]
lista_B = [2, 3, 4, 4, 5, 6, 7, 8]

A = set(lista_A)
B = set(lista_B)

if( len(A - B) == 0 ):
    print('A dentro B')
elif( len(B - A) == 0 ):
    print('B dentro A')
else:
    print('ninguna esta dentro')

# Ejercicio 4

A = {1, 3, 5, 7}
B = {1, 2, 3, 6}
C = {3, 4, 5, 8}

print(F"Intersección \n{A & B & C}")
print(F"Union \n{A | B | C}")
D = (A | B | C) - ((A & B)  | (A & C) | (C & B))
print(F"Diferencia Simetrica \n{D}")