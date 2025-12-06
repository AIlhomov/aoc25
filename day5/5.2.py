read_file = open("input.txt", "r")
lines = read_file.readlines()

fresh_food = []
stop = False
res = 0

allRanges = []

for line in lines:

    rangeFood = line.strip('\n')
    #print(rangeFood)

    
    if not stop:
        if line == '\n':
            stop = True #now comes the food ID:s
            continue

        if rangeFood == '':
            continue
        
        fromm, to = rangeFood.split('-')

        allRanges.append([int(fromm), int(to)])

        #We dont care about ID:s in part 2

allRanges.sort(key=lambda interval: interval[0])
merged = [allRanges[0]]
for current in allRanges:
    previous = merged[-1]
    if current[0] <= previous[1]:
        previous[1] = max(previous[1], current[1])
    else:
        merged.append(current)

#print(merged)
res = 0
for start, end in merged:
    res += end - start + 1
print(res)
