import sqlite3

def obtener_estudiantes():
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Estudiante')
    return list(cur)

def obtener_materias():
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Materia')
    return list(cur)

def agregar_estudiante(nombre, apellido):
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO Estudiante (nombre, apellido) VALUES (?, ?)', (nombre, apellido))
    conn.commit()

def eliminar_estudiante(nombre, apellido):
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute(f"DELETE FROM Estudiante WHERE nombre='{nombre}' AND apellido='{apellido}'")
    conn.commit()

def obtener_profesores():
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Profesor')
    return list(cur)

def asignar_materia_profesor(id_profesor, id_materia):
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO Dictando (id_profesor, id_materia) VALUES (?, ?)', (id_profesor, id_materia))
    conn.commit()

def inscribir_estudiante(id_estudiante, id_dictado):
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute('INSERT INTO Cursando (id_estudiante, id_dictado) VALUES (?, ?)', (id_estudiante, id_dictado))
    conn.commit()

# agregar_estudiante('Maria', 'Galindo')
# eliminar_estudiante('Maria', 'Galindo')
print(obtener_estudiantes())
print(obtener_materias())
print(obtener_profesores())
# asignar_materia_profesor(1, 1)
# asignar_materia_profesor(1, 2)

inscribir_estudiante(1, 1)
inscribir_estudiante(1, 2)
inscribir_estudiante(2, 1)
inscribir_estudiante(2, 2)
inscribir_estudiante(3, 1)
inscribir_estudiante(4, 2)