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
def reynolds ():
    re = (9 * 0.875)/(.0015)
    print('Reynolds number is', re)
reynolds()

def wavelength ():
    wv = (2 * .028)*(math.sin(math.radians(35)))
    print('Wavelength is', wv, 'nm')
wavelength()

def prodrate ():
    pd = (100/(1+(0.8*2*10))**(1/.8))
    print('Production rate is', pd, 'barrels/day')
prodrate()

def velocity():
    cv = (2028* math.log(11000/8300))
    print('Change of velocity is', cv, 'm/s')
velocity()