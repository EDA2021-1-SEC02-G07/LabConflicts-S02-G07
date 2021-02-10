import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def loadBooks(filename):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = cf.data_dir + filename
    return model.addBooks(booksfile)


def loadTags(filename):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + filename
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    tags = model.createTagList()
    for tag in input_file:
        model.addTag(tags, tag)
    return tags


def loadBooksTags(filename):
    # TO-DO: Modificación de Est-1 y Est-2 en el Lab 2
    booktagsfile = cf.data_dir + filename
    return model.addBooksTags(booktagsfile)
    btfile = cf.data_dir + filename
    return model.addBooksTags(btfile)

"Hola mario como estás yo estoy muy cansada tengo sueño " "123"