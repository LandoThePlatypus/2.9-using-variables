# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

import math
#balls
print('This program calculates the Reynolds number given velocity, length, and viscosity')
ve = float(input('Please enter the velocity (m/s):'))
len = float(input('Please enter the length (m):'))
vis = float(input('Please enter the viscosity (m^2/s):'))


def reynolds ():
    re = (ve* len)/(vis)
    print(f'Reynolds number is {re:.0f}')
reynolds()

print('This program calculates the wavelength given distance and angle')
dis = float(input('Please enter the distance (nm):'))
angle = float(input('Please enter the angle (degrees):'))

def wavelength ():
    wv = (2 * dis)*(math.sin(math.radians(angle)))
    print(f'Wavelength is {wv:.4f} nm')
wavelength()

print('This program calculates the production rate given time, initial rate, and decline rate')
time =float(input('Please enter the time (days):'))
irate =float(input('Please enter the initial rate (barrels/day):'))
drate =float(input('Please enter the decline rate (1/day):'))

def prodrate ():
    pd = (irate/(1+(.8*drate*time))**(1/.8))
    print(f'Production rate is {pd:.2f} barrels/day')
prodrate()

print('This program calculates the change of velocity given initial mass, final mass, and exhaust velocity')
mint = float(input('Please enter the initial mass (kg):'))
mfin = float(input('Please enter the final mass (kg):'))
ev = float(input('Please enter the exhaust velocity (m/s):'))

def velocity():
    cv = (ev* math.log(mint/mfin))
    print(f'Change of velocity is {cv:.1f} m/s')
velocity()