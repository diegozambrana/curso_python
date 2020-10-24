import sqlite3

def materias_cursadas(nombre, apellido):
    sql = f"""
        SELECT
            Estudiante.nombre, Estudiante.apellido, Materia.nombre,
            Cursando.primer_parcial, Cursando.segundo_parcial, Cursando.nota_final
        FROM
            Estudiante 
        INNER JOIN Cursando 
            ON Estudiante.id_estudiante = Cursando.id_estudiante
        INNER JOIN Dictando
            ON Cursando.id_dictado = Dictando.id_dictando
        INNER JOIN Materia
            ON Materia.id_materia = Dictando.id_materia
        WHERE
            Estudiante.nombre = '{nombre}' AND Estudiante.apellido = '{apellido}'
    """
    conn = sqlite3.connect('db/ejemplo.sqlite')
    cur = conn.cursor()
    cur.execute(sql)
    return list(cur)

print(materias_cursadas('Pedro', 'Martinez'))

