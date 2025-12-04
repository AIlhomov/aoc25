read_file = open("input.txt", "r")
lines = read_file.readlines()

res = 0
import heapq

for line in lines:
    maxVal = 0 #find biggest val then just take the next biggest after it.
    allValsinLine = []
    addThis = 0
    for digit in line:
        if digit == '\n':
            continue
        digit = int(digit)
        allValsinLine.append(digit)
        maxVal = max(maxVal, digit)
    #find its pos
    i = 0
    for digit in line:
        if digit == '\n':
            continue
        digit = int(digit)
        if maxVal == digit:
            break
        i += 1
    secondBiggest = 0
    if i == len(line)-2: #whoops a problem
        #just take the second biggest then.
        biggest2 = heapq.nlargest(2, allValsinLine)
        addThis = int(str(biggest2[1]) + str(maxVal))
        #print('AAA')
    else:
        #find second biggest from i -> ..
        for i in range(i+1, len(line)):
            if line[i] == '\n':
                continue
            digit = int(line[i])
            secondBiggest = max(secondBiggest, digit)
        addThis = int(str(maxVal) + str(secondBiggest))
    res += addThis
    #print(res)
    #print(maxVal, i)
print(res)