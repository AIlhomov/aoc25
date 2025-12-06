read_file = open("input.txt", "r")
lines = read_file.readlines()

fresh_food = []
stop = False
res = 0

for line in lines:

    rangeFood = line.strip('\n')
    #print(rangeFood)

    if not stop:
        fresh_food.append(rangeFood)

    if line == '\n':
        stop = True #now comes the food ID:s
    
    if stop:
        #now rangeFood becomes ID:s AYYAAYYAAYAY
        if rangeFood == '':
            continue
        
        id = int(rangeFood)

        for i in range(len(fresh_food)-1):
            fromm, to = fresh_food[i].split('-')
            
            if id >= int(fromm) and id <= int(to):
                res += 1
                break #WOWOWOWOW AINT NO WAY
print(res)
        #print(fresh_food)
        #print("here", rangeFood)
