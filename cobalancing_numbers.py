# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#nuts

n = int(input('Enter a value for n:'))
bal_1=0
r=1
bal_2= n + r


for i in range(1, n+2):
    bal_1+=i

while bal_2 < bal_1:
    bal_2 += (n+r)
    r+=1


if bal_1 == bal_2:
    print(f'{n} is a co-balancing number with r={r-1}')
else:
    print(f'{n} is not a co-balancing number')