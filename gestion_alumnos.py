from gestion_archivos import *

nombre_archivo = "alumnos.json"

lista_de_alumnos = importar_json(nombre_archivo)

l = []

for alumno in lista_de_alumnos:
    d = {}

    media = sum(alumno["notas"])/len(alumno["notas"])

    d["id"] = alumno["id"]
    d["nombre"] = alumno["nombre"] 
    d["apellidos"] = alumno["apellidos"]
    d["edad"] = alumno["edad"]
    d["notas"] = alumno["notas"]
    d["nota_media"] = media
    d["faltas"] = alumno["faltas"]
    d["supera"] = alumno["supera"]
    
    l.append(d)

exportar_json(l, "alumnos_con_media2.json")
