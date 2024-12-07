# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#hehe

passports = open(input("Enter the name of the file: "), "r")
allpassports = passports.read()
passports.close()

ppts = allpassports.split('\n\n')

necessary_fields = ["byr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

valid_passport_count = 0
valid_passports = [] 
for ppt in ppts:
    is_valid = True
    for field in necessary_fields:
        if field not in ppt:
            is_valid = False
            break
    if is_valid:
        valid_passport_count += 1
        valid_passports.append(ppt)

print(f"There are {valid_passport_count} valid passports")

file = open('valid_passports.txt', 'w')
for valid_passport in valid_passports:
    file.write(valid_passport + '\n\n')
file.close()
