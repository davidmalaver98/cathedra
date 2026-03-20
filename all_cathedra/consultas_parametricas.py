
from conexion_cathedra import conexion
cursor = conexion.cursor()
# consulta 1
consulta = """
SELECT u.nombre, u.apellido, r.nombre_rol
FROM usuarios u
JOIN roles r ON u.id_rol = r.id_rol
"""

cursor.execute(consulta)
resultado = cursor.fetchall()
print("consulta #1: ",resultado)

# consulta 2
consulta = """
SELECT nombre_beca, porcentaje_cobertura, estado
FROM becas
WHERE porcentaje_cobertura >= %s
"""

porcentaje = 80

cursor.execute(consulta, (porcentaje,))
resultado = cursor.fetchall()

print("consulta #2: ",resultado)

# consulta 3

consulta = """
SELECT b.nombre_beca, p.fecha_postulacion, p.estado
FROM postulaciones p
JOIN becas b ON p.id_beca = b.id_beca
WHERE p.id_usuario = %s
"""

id_usuario = 2

cursor.execute(consulta, (id_usuario,))
resultado = cursor.fetchall()

print("consulta #2:",resultado)

