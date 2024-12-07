# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20
import math
from math import sqrt
side = float(input('Please enter the side length:'))
#nuts

def printresult():
    pass
tri = (side**2) * ( sqrt(3)/4)
square = side**2
penta = (side**2)*(1/4)*(sqrt(5*(5 + 2 * sqrt(5))))
hex = (side**2)*(3/2)*(sqrt(3))
dodec = 3 * (side**2) * (2 + sqrt(3))
printresult()
print(f'A triangle with side {side:.2f} has area  {tri:.3f}')
print(f'A square with side {side:.2f} has area  {square:.3f}')
print(f'A pentagon with side {side:.2f} has area  {penta:.3f}')
print(f'A hexagon with side {side:.2f} has area  {hex:.3f}')
print(f'A dodecagon with side {side:.2f} has area  {dodec:.3f}')