# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

int_1 = int(input('Enter an integer:'))
int_2 = int(input('Enter another integer:'))
#hehe
i=int_1
total=0
for i in range(int_1,int_2+1):
    total += i

print(f'The sum of all integers from {int_1} to {int_2} is {total}')