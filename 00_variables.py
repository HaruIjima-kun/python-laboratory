'''
    ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
    - Recuerda que todas las instrucciones de participación están en el
    repositorio de GitHub.

    Lo primero... ¿Ya has elegido un lenguaje?
    - No todos son iguales, pero sus fundamentos suelen ser comunes.
    - Este primer reto te servirá para familiarizarte con la forma de participar
    enviando tus propias soluciones.

    EJERCICIO:
    - Crea un comentario en el código y coloca la URL del sitio web oficial del
    lenguaje de programación que has seleccionado.
    - Representa las diferentes sintaxis que existen de crear comentarios
    en el lenguaje (en una línea, varias...).
    - Crea una variable (y una constante si el lenguaje lo soporta).
    - Crea variables representando todos los tipos de datos primitivos
    del lenguaje (cadenas de texto, enteros, booleanos...).
    - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"

    ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
    debemos comenzar por el principio.

'''

# ==================== Comentario en una línea ====================
# Esto es un comentario en una sola línea https://python-docs-es.readthedocs.io/es/3.12/


# ==================== Diferentes sintaxis para crear comentarios: ====================
# Esto es un comentario en línea
'''
    Este es un comentario en varias líneas con comillas simples
    https://python-docs-es.readthedocs.io/es/3.12/
'''

"""
    Este es un comentario en varias líneas con comillas dobles
    https://python-docs-es.readthedocs.io/es/3.12/
"""


# ==================== Crear una variable y una constante ====================
my_var = 42
print(my_var)

my_const = 42
print(my_const)


# ============== Variables representando todos los tipos de datos primitivos ==============
# Entero
my_int = 42

# FLoat
my_float = 3.1418

# String / cadena de texto
my_string = "Hola mundo!"

# Booleano
my_bool = True

# Lista
my_list = [0,1,2,3,4,5,6,7,8,9]

# Tupla
my_tuple = (0,1,2,3,4,5,6,7,8,9)

# Set (conjunto)
my_set = {0,1,2,3,4,5,6,7,8,9}

# Diccionario
my_dict = {'key1': 'value1', 'key2': 'value2'}

# noneType
my_null = None

# Imprimir los valores
print("Int:", my_int)
print("Float:", my_float)
print("String:", my_string)
print("Bool:", my_bool)
print("List:", my_list)
print("Tuple:", my_tuple)
print("Set:", my_set)
print("Dict:", my_dict)
print("NoneType:", my_null)