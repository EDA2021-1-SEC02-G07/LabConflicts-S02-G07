import config as cf
from DISClib.ADT import list as lt
assert cf

"""
En el modelo, se crean las estructuras de datos, es decir,
las variables donde se van a guardar los datos leidos de los
archivos CSV.

El modelo debe ser el unico sitio donde se modifican y manipulan
los datos.
"""


def addBooks(booksfile):
    """
    Para guardar los libros provenientes del archivo CSV
    vamos a crear una lista, en donde quedarán todos los datos.

    No es importante entender como funciona esta lista por ahora.

    La funcion newList crea una lista de muchas formas.  Una de ellas
    es leyendo todo lo que encuentre en el archivo indicado por filename.
    Cada linea del archivo quedará en una posicion de la lista.
    """
    books = lt.newList(datastructure='SINGLE_LINKED',
                       filename=booksfile)
    return books


def addTag(taglist, tag):
    """
    Para procesar el archivo de tags vamos a usar de otra forma la lista.
    En este caso, agregaremos cada linea del archivo a la lista, en lugar
    de usar la opcion de crearla con el nombre del archivo.
    """
    lt.addLast(taglist, tag)


def createTagList():
    """
    Esta funcion crea una lista vacia.  Esta lista se utilizara
    para ir guardando la informacion en el archivo de tags.
    """
    taglist = lt.newList(datastructure='SINGLE_LINKED')
    return taglist

def addBookTags(booktagsfile):
    # TO-DO: Modificación de Est-1 y Est-2 en el Lab 2
    booktags = lt.newList(datastructure='SINGLE_LINKED',
                            filename=booktagsfile)
    return booktags
    bts = lt.newList(datastructure='SINGLE_LINKED',filename=booktagsfile)
    return bts
