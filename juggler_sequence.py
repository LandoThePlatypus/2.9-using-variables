# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#nuts
import math
from math import sqrt
itera = int(input('Enter a positive integer:'))
i = 1
start = itera
jugg = []
while i == 1:
    jugg.append(itera)
    if itera == 1:
        i = 0
    elif itera %2 == 0:
        itera = int(itera**(1/2))
    else:
        itera = int(itera**(3/2))

print(f'The Juggler sequence starting at {start} is: {", ".join( repr(e) for e in jugg)}')
print(f'It took {(len(jugg)-1)} iterations to reach 1')