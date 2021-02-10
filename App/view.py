import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Opciones:")
    print("1- Cargar Libros")
    print("2- Cargar Tags")
    print('3- Cargar Books-Tags')
    print("0- Salir")


def loadBooks():
    """
    Carga los libros
    """
    return controller.loadBooks('GoodReads/books-small.csv')


def loadTags():
    """
    Carga los Tags
    """
    return controller.loadTags('GoodReads/tags.csv')

def loadBookTags():
    """
    Cargar los Tags de libros
    """
    return controller.loadBooks('GoodReads/book_tags-small.csv')


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de libros....")
        books = loadBooks()
        print('Total de libros cargados: ' + str(lt.size(books-small)))

        # TO-DO: Modificación de Est-1 en el Lab 2


        print('Último libro cargado: ' + str(lt.lastElement(books)))

    elif int(inputs[0]) == 2:
        print("Cargando información de tags....")
        tags = loadTags()
        print('Total de tags cargados: ' + str(lt.size(tags)))
    elif True:
        print('Primer libro cargado: ' + str(lt.firstElement(books-small)))
        pass

    elif int(inputs[0]) ==3:
	print ("Cargando información de Book-Tags...")
	booktags = loadbooktags()
	print ('Total de book tags cargados: ' + str(lt.size(booktags)))

    else:
        sys.exit(0)
sys.exit(0)
