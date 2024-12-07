# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#hehe

#input from the user
input_str = input("Enter numbers: ")
#Split the input string into list of integers
numbers = [int(x) for x in input_str.split()]
#Initialize variables for left and right portions
left = []
right = []
#Calculate the total sum
total_sum = 0
for num in numbers:
    total_sum += num
#Find the split point
found_split = False
current_sum = 0
for i in range(len(numbers)):
    left = numbers[:i]
    right = numbers[i:]
    current_sum = 0
    for num in left:
        current_sum += num
    if current_sum * 2 == total_sum:
        found_split = True
        break
#Print
if found_split:
    print("Left:", left)
    print("Right:", right)
    print("Both sum to", current_sum)
else:
    print("Cannot split evenly")