# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

import math

temp = float(input('Enter the excess temperature:'))

def slope(x0, y0, x1, y1):
    return ((math.log10(y1 / y0)) / (math.log10(x1 / x0)))

def equation(y0, x, x0, m):
    return (y0 * ((x / x0)**m))

# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum
# cum

if 1.3 <= temp < 5:
    line_slope = slope(1.3, 1000, 5, 7000)
elif 5 <= temp < 30:
    line_slope = slope(5, 7000, 30, 1500000)
elif 30 <= temp < 120:
    line_slope = slope(30, 1500000, 120, 25000)
elif 120 <= temp <= 1200:
    line_slope = slope(120, 25000, 1200, 1500000)
else:
    print('Surface heat flux is not available')

if 1.3 <= temp <5:
    flux = equation(1000, temp, 1.3, line_slope)
elif 5<= temp <30:
    flux = equation(7000, temp, 5, line_slope)
elif 30<= temp <120:
    flux = equation(1500000, temp, 30, line_slope)
elif 120<= temp <=1200:
    flux = equation(25000, temp, 120, line_slope)

print(f'\nThe surface heat flux is approximately {flux:.0f} W/m^2')