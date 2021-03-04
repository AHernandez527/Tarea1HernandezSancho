# Programa Tester de módulos
# Adriana Hernández - Alejandro Sancho
# Primero se comienza importando las funciones

from programa1_micros import CheckChar
from programa1_micros import CapsSw
# En esta lista se encuentran todos los escenarios de letra que se prueban
lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

# El ciclo for va a probar con i cada valor de la lista en las funciones
for i in lista1:
    print(CheckChar(i))
for i in lista1:
    CapsSw(i)
CheckChar('abc')  # Caso para error de multiples caracteres
CheckChar('a1b')  # Caso para error de caracteres no alfabeticos
CheckChar(123)  # Caso para error de elemento no str
