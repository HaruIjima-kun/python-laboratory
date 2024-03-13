'''
    EJERCICIO:
    - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
    (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
    - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
    - Debes hacer print por consola del resultado de todos los ejemplos.

    DIFICULTAD EXTRA (opcional):
    Crea un programa que imprima por consola todos los números comprendidos
    entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

    Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
'''

# Ejemplos de operadores
print("===== Tomando como valores a = 10 y b = 3 =====")
a = 10
b = 3

# Operadores aritméticos
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
modulo = a % b
potencia = a ** b

print("\n     OPERADORES ARITMÉTICOS")
print("El resultado de a + b =", suma)
print("El resultado de a - b =", resta)
print("El resultado de a * b =", multiplicacion)
print("El resultado de a / b =", division)
print("El resultado de a // b =", division_entera)
print("El resultado de a % b =", modulo)
print("El resultado de a ** b =", potencia)



# Operadores de comparación
igual = (a == b)
distinto = (a != b)
mayor_que = (a > b)
menor_que = (a < b)
mayor_o_igual_que = (a >= b)
menor_o_igual_que = (a <= b)

print("\n     OPERADORES DE COMPARACIÓN")
print("El resultado de a == b =", igual)
print("El resultado de a != b =", distinto)
print("El resultado de a > b =", mayor_que)
print("El resultado de a < b =", menor_que)
print("El resultado de a >= b =", mayor_o_igual_que)
print("El resultado de a <= b =", menor_o_igual_que)

# Operadores lógicos
and_logic = (a > b) and (b > 0)
or_logic = (a > b) or (b > 0)
not_logic = not (a > 0)

print("\n     OPERADORES LÓGICOS")
print("El resultado de (a > b) and (b > 0) = ", and_logic)
print("El resultado de (a > b) or (b > 0) = ", or_logic)
print("El resultado de not (a > 0) = ", not_logic)

# Operadores de asignación
print("\n     OPERADORES DE ASIGNACIÓN")
c = a   # Asignación simple
print("El resultado de c = a es que c =", c)

c += 5  # Suma y asignación ->  c = c + 5
print("El resultado de c += 5 es que c =", c)

c -= 3  # Resta y asignación -> c = c - 3
print("El resultado de c -= 3 es que c =", c)

c *= 2  # Multiplicación y asignación -> c = c * 2
print("El resultado de c *= 2 es que c =", c)

c /= 4  # División y asignación -> c = c / 4
print("El resultado de c /= 4 es que c =", c)

c //= 4  # División entera y asignación -> c = c // 4
print("El resultado de c //= 4 es que c =", c)


# Operadores de identidad
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
es_mismo_objeto = lista1 is lista2
no_es_mismo_objeto = lista1 is not lista2

print("\n     OPERADORES DE IDENTIDAD")
print("El resultado de lista1 is lista2 =", es_mismo_objeto)
print("El resultado de lista1 is not lista2 =", no_es_mismo_objeto)

# Operadores de membresía
en_lista = 1 in lista1
no_en_lista = 4 not in lista1

print("\n     OPERADORES DE MEMBRESÍA")
print("El resultado de 1 in lista1 =", en_lista)
print("El resultado de 4 not in lista1 =", no_en_lista)

# Operadores de bits
a = 10  # Representación binaria: 0b0101
b = 3  # Representación binaria: 0b0011

bitwise_and = a & b     # Representación binaria del resultado: 0b0001 (decimal: 1) 
bitwise_or = a | b      # Representación binaria del resultado: 0b0111 (decimal: 7)
bitwise_xor = a ^ b     # Representación binaria del resultado: 0b0110 (decimal: 6)
bitwise_not = -a        # Representación binaria del resultado: (varía según la representación interna del número en binario)
left_shift = a << 1     # Representación binaria del resultado: 0b1010 (decimal: 10)
right_shift = a >> 1    # Representación binaria del resultado: 0b0010 (decimal: 2)


print("\n     OPERADORES DE BITS")
print("El resultado de a & b =", bitwise_and)
print("El resultado de a | b =", bitwise_or)
print("El resultado de a ^ b =", bitwise_xor)
print("El resultado de -a =", bitwise_not)
print("El resultado de a << 1 =", left_shift)
print("El resultado de a >> 1 =", right_shift)