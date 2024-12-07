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
i = 1
#hehe
for i in range(1,101):
    if i % int_1 == 0:
        if i % int_2 == 0:
            print('Howdy Whoop')
        else:
            print('Howdy')
        i += 1
    elif i % int_2 == 0:
        print('Whoop')
        i += 1
    else:
        print(i)
        i += 1
