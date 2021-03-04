# Programa de definición de Módulos Adriana Hernández - Alejandro Sancho
def CheckChar(string):
    # Esta función es la encargada de revisar qué hay en la entrada
    b = 0
    if type(string) != str:
        # Aquí revisa si el dato es un string y lanza el
        # error en caso de que no lo sea
        print('/* E03 Tipo de dato inválido*/')

    elif len(string) == 1:
        # Una vez probado que es string, aquí se fija si solo tiene 1 caracter
        if string.isalpha() == 1:
            # Y aquí revisa si ese único caracter es una letra
            return 0  # Si es una letra la función retornará el 0

    elif len(string) > 1:
        # Si tiene más de un caracter se quedará aquí
        for i in string:
            if i.isalpha() == 1:
                # Utiliza el contador b, si el elemento es letra no cambia nada
                b = b
            elif i.isalpha() == 0:
                # Y aquí si no es letra cambiará a b de su valor inicial de 0
                b = b + 1
        if b == 0:  # según el valor de b esta parte decidirá qué error imprime
            print('/* E01 Múltiples valores insertados*/')
            # Error para el caso de que sean solo letras pero más de un
            # elemento en el string

        if b > 0:
            print('/* E02 Valores insertados no alfabéticos*/')
            # Error para elementos que no sean letras


def CapsSw(entrada):
    # Se crea la función que cambiará la capitalización de las letras
    if CheckChar(entrada) == 0:
        # Esto le dirá según la función anterior si se tiene un solo
        # elemento y del tipo str
        print(entrada.swapcase())
        # Si es así, esta parte le invierte la capitalización
    else:
        print(CheckChar(entrada))
        # Si no es así, esta parte devolverá el error según la
        # función CheckChar
