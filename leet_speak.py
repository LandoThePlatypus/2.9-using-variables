# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#nuts

text = str(input('Enter some text:'))

leet ={
    'a':'4',
    'e':'3',
    'o':'0',
    's':'5',
    't':'7'
}
def replace_chars(string, replacements):
    return ''.join(replacements.get(char, char) for char in string)

new_string = replace_chars(text, leet)

print(f'In leet speak, "{text}" is: {new_string}')