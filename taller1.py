#Esta funcion verifica si una cadena pertenece a un lenguaje dado
def verificar_cadena_lenguaje(lenguaje: set, cadena: str) -> bool:

    for palabra in lenguaje:
        if palabra == cadena:
            return True

    return False

#La cadena debe tener exactamente 6 caracteres de longitud
def verificar_pertenencia_regla_uno(lenguaje: set, cadena: str) -> bool:

    return True if len(cadena) == 6 and verificar_cadena_lenguaje(lenguaje=lenguaje, cadena=cadena) else False

def main():
    return verificar_pertenencia_regla_uno(set({"aa", "bb", "cc", "aaaaaa"}), "aaaaaa")

if __name__=='__main__':
    print(main())