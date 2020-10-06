"""
la formula para obtener la aceleracion es la siguiente:
a = dv / dt = (vf – vi)/(tf – ti)
"""

v0 = 12.3  # velocidad inicial en m/s
v1 = 41.2  # velocidad final en m/s
t0 = 0     # Tiempo inicial en segundos
t1 = 10    # Tiempo Final en segundos

# Aceleración se representa en m/s2
a = (v1 - v0)/t

print('la aceleración es {} m/s2'.format(a))