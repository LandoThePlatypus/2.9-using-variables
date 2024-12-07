# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Landon Jaffe
# Section:      102-536
# Assignment:   Lab 3.17
# Date:         05 09 20

#hehe

def opengame():
    #Open the game file and read the instructions
    with open('game.txt') as myfile:
        #split on \n, can also use myfile.readlines()
        instructions = myfile.read().split('\n')
    return instructions

def makefile(ind,instr):
    #Open new file to write coin info
    with open('coins.txt','w') as newfile:
        for i in ind:
            #loop through instructions in order followed
            if instr[i][:4] == 'coin':
                #write coin data
                if instr[i][5] == '-':
                    newfile.write(instr[i][5:] + '\n')
                else:
                    #if +, only write number, not +
                    newfile.write(instr[i][6:] + '\n')

def ops(inst, num, coins, i, ind):
    #Do line operation
    if inst == 'coin':
        #add to total, move to next line
        coins += int(num)
        ind.append(i)
        i += 1
    elif inst == 'none':
        #move to next line
        ind.append(i)
        i += 1
    else:
        #jump to next operation
        ind.append(i)
        i += int(num)
    return coins, i, ind


#main code
#first, open the game file and read the instructions
instr = opengame()
#initialize counters and keep track of order of instructions
coins = 0
ind = []
i = 0
while i not in ind:
    #split operation and signed number on space
    inst, num = instr[i].split()
    #do operation
    coins, i, ind = ops(inst, num, coins, i, ind)
    if i >= len(instr):
        #end of program
        #print( 'end of file') for testing
        break
#print coint total
print(f'Total coins collected: {coins}')

makefile(ind, instr)