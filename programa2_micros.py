# ERR2 -2.5
# Programa Tester de módulos
# Adriana Hernández - Alejandro Sancho
# Primero se comienza importando las funciones
from programa1_micros import CheckChar
from programa1_micros import CapsSw
# En esta lista se encuentran todos los escenarios de letra que se prueban
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

# El ciclo for va a probar con i cada valor de la lista en las funciones
for i in lista1:

    def test_answer1():  # Codigo de prueba con pytest para salida en 0
        assert CheckChar(i) == 0

for i in lista1:

    def test_answer2():  # Prueba de que se invierten capitalizaciones
        CapsSw(i) == i.swapcase


def test_answer3():  # Codigo de prueba con pytest para multiples caracteres
    assert CheckChar('abc') == print('/* E01 Múltiples valores insertados*/')


def test_answer4():  # Codigo de prueba con pytest para caracteres no letra
    assert CheckChar('a1c') == print('/* E02 Valores insertados no alfabéticos*/')


def test_answer5():  # Codigo de prueba con pytest para elemento no string
    assert CheckChar(123) == print('/* E03 Tipo de dato inválido*/')

# Para realizar las pruebas, dirigirse al cmd, ubicarse en la dirección de
# la carpeta y escribir "pytest Programa2_micros"


# Si bien los metodos estan mal, el test si evalua correctamente considerando
# este error, por eso no quito puntos
