# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

import math

x= float(input('Enter a value for x: '))

while  not(0 < x <= 2):
    try_a = float(input('Out of range! Try again: '))
    x = try_a
#reee

error = float(input('Enter the tolerance: '))
print('\n')
expo= 2
total=x-1

while True:
    taylor =((x -1)**(expo)/(expo))
    if abs(taylor) < error:
        break
    else:
        pass
    if expo %2 ==0:
        total -= taylor
    else:
        total += taylor
    expo = expo + 1

print(f'ln({x}) is approximately {total}')
print(f'ln({x}) is exactly {math.log(x)}')
print(f'The difference is {abs(total - math.log(x))}')