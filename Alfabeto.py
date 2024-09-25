
def main():
    print("1. Generar Cadenas")
    lenguaje : list = []
    generar_permutaciones("", ["xy","an","ox"], 10, lenguaje)
    print(lenguaje)
   # print(len(lenguaje))
    print("\n")

    print("2. Verificar si una palabra pertenece a un Lenguaje")
    print(verificar_cadena_lenguaje(lenguaje, "xyxy"))
    print("\n")

    print("3. Verificar si una cadena pertenece a un lenguaje y establecer una regla [6 caracteres de longitud]")
    print(verificar_pertenencia_regla_uno(lenguaje, "xyxy"))
    print("\n")

    print("4. Generar cadenas de palabras con un sufijo/prefijo especifico a partir de un alfabeto")
    print(generar_cadenas_prefijo("pref", ["xy","an","ox"], 10))
    print(generar_cadenas_sufijo("pos", ["xy","an","ox"], 10))

#Funcion para generar cadenas de palabras con prefijos a partir de un alfabeto
def generar_cadenas_prefijo(prefijo, alfabeto, num_caracteres):
    palabras_alfabeto = []
    generar_permutaciones("", alfabeto, num_caracteres, palabras_alfabeto)
    palabras_prefijo = []

    for palabra in palabras_alfabeto:
        palabras_prefijo.append(prefijo + palabra)

    return palabras_prefijo


#Funcion para generar cadenas de palabras con prefijos a partir de un alfabeto
def generar_cadenas_sufijo(sufijo, alfabeto, num_caracteres):
    palabras_alfabeto = []
    generar_permutaciones("", alfabeto, num_caracteres, palabras_alfabeto)
    palabras_sufijo = []

    for palabra in palabras_alfabeto:
        palabras_sufijo.append(palabra + sufijo)

    return palabras_sufijo


def generar_permutaciones(palabra_actual, alfabeto, num_max, lenguaje: list) -> None:
    """ Genera las permutaciones de palabras con los caracteres dados con un número máximo de caracteres 'n' """

    if palabra_actual:  #Si la palabra actual no está vacía, entonces ->
        lenguaje.append(palabra_actual)

    #Si la palabra obtiene el número máximo de caracteres, se detiene la ejecución
    if len(palabra_actual) == num_max:
        return

    #Metodo recursivo
    for char in alfabeto:
        generar_permutaciones(palabra_actual + char, alfabeto, num_max, lenguaje)

#Esta funcion verifica si una cadena pertenece a un lenguaje dado
def verificar_cadena_lenguaje(lenguaje: set, cadena: str) -> bool:

    for palabra in lenguaje:
        if palabra == cadena:
            return True

    return False

#La cadena debe tener exactamente 6 caracteres de longitud
def verificar_pertenencia_regla_uno(lenguaje: set, cadena: str) -> bool:

    return True if len(cadena) == 6 and verificar_cadena_lenguaje(lenguaje=lenguaje, cadena=cadena) else False


main()
