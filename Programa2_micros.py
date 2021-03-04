# Programa Tester de módulos
# Adriana Hernández - Alejandro Sancho

from programa1_micros import CheckChar
from programa1_micros import CapsSw

lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

for i in lista1:
    print(CheckChar(i))
for i in lista1:
    CapsSw(i)
CheckChar('abc')
CheckChar('a1b')
CheckChar(123)
