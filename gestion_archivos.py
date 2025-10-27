import csv
import os

def de_lista_a_csv(l, nombre_fichero):
    """
    Crea o actualiza un archivo CSV a partir de una lista de diccionarios.

    Parámetros:
    -----------
    l : list[dict]
        Lista de diccionarios con claves de tipo cadena (columnas) y valores también de tipo cadena.
        Ejemplo: [{"nombre": "Ana", "edad": "30"}, {"nombre": "Luis", "edad": "25"}]

    nombre_fichero : str
        Nombre (o ruta) del archivo CSV a crear o actualizar.

    Comportamiento:
    ---------------
    - Si el archivo no existe:
        * Se crea un nuevo CSV con las claves del primer diccionario como encabezados.
        * Se muestran las columnas creadas en un mensaje.

    - Si el archivo ya existe:
        * Se comprueba que las columnas coinciden con las claves de los diccionarios.
        * Si coinciden, se añaden las nuevas filas al final del archivo.
        * Si no coinciden, se muestra un mensaje de error sin modificar el archivo.
    """

    # Comprobamos que la lista no esté vacía
    if not l:
        print("La lista está vacía. No se ha creado ni modificado ningún archivo.")
        return

    # Obtenemos las claves del primer diccionario
    columnas = list(l[0].keys())

    # Verificamos si el archivo ya existe
    if os.path.exists(nombre_fichero):
        with open(nombre_fichero, newline='', encoding='utf-8') as csvfile:
            lector = csv.reader(csvfile)
            encabezado = next(lector, None)

        # Comprobamos si las columnas coinciden
        if encabezado != columnas:
            print("❌ Error: Las columnas no coinciden con las del archivo existente.")
            return

        # Añadimos los datos si las columnas coinciden
        with open(nombre_fichero, 'a', newline='', encoding='utf-8') as csvfile:
            escritor = csv.DictWriter(csvfile, fieldnames=columnas)
            escritor.writerows(l)
        print(f"✅ Datos añadidos correctamente al archivo existente: '{nombre_fichero}'")

    else:
        # Creamos un nuevo archivo CSV
        with open(nombre_fichero, 'w', newline='', encoding='utf-8') as csvfile:
            escritor = csv.DictWriter(csvfile, fieldnames=columnas)
            escritor.writeheader()
            escritor.writerows(l)
        print(f"🆕 Archivo '{nombre_fichero}' creado con las columnas: {', '.join(columnas)}")
