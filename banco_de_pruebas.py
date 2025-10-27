from gestion_archivos import *


datos = [
    {"nombre": "Ana", "edad": "30", "ciudad": "Madrid"},
    {"nombre": "Luis", "edad": "25", "ciudad": "Sevilla"}
]

datos2 = [
    {"nombre": "Ana", "edad": "30" },
    {"nombre": "Luis", "edad": "25" }
]

de_lista_a_csv(datos, "personas.csv")
 
