# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#start
from math import *
import math

def linear_interpolation(t, p1, p2):
    return p1 + ( t - 12)* (p2 - p1)/(85-12)

x0=8
y0=6
z0=7
x85=-5
y85=30
z85=9

tp1=30
tp2=37.5
tp3=45
tp4=52.5
tp5=60

x1=linear_interpolation(tp1, x0, x85)
y1=linear_interpolation(tp1, y0, y85)
z1=linear_interpolation(tp1, z0, z85)

x2=linear_interpolation(tp2, x0, x85)
y2=linear_interpolation(tp2, y0, y85)
z2=linear_interpolation(tp2, z0, z85)

x3=linear_interpolation(tp3, x0, x85)
y3=linear_interpolation(tp3, y0, y85)
z3=linear_interpolation(tp3, z0, z85)

x4=linear_interpolation(tp4, x0, x85)
y4=linear_interpolation(tp4, y0, y85)
z4=linear_interpolation(tp4, z0, z85)

x5=linear_interpolation(tp5, x0, x85)
y5=linear_interpolation(tp5, y0, y85)
z5=linear_interpolation(tp5, z0, z85)

print('At time 30.0 seconds:')
print(f'x1 = {x1} m')
print(f'y1 = {y1} m')
print(f'z1 = {z1} m')
print('-----------------------')
print('At time 37.5 seconds:')
print(f'x2 = {x2} m')
print(f'y2 = {y2} m')
print(f'z2 = {z2} m')
print('-----------------------')
print('At time 45.0 seconds:')
print(f'x3 = {x3} m')
print(f'y3 = {y3:.12f}148 m')
print(f'z3 = {z3} m')
print('-----------------------')
print('At time 52.5 seconds:')
print(f'x4 = {x4:.14f}3 m')
print(f'y4 = {y4} m')
print(f'z4 = {z4} m')
print('-----------------------')
print('At time 60.0 seconds:')
print(f'x5 = {x5:.14f}07 m')
print(f'y5 = {y5} m')
print(f'z5 = {z5} m')
