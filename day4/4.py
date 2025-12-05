
i = 0
j = 0
res = 0

#grid = ['..@@.@@@@.', '@@@.@.@.@@', '@@@@@.@.@@', '@.@@@@..@.', '@@.@@@@.@@', '.@@@@@@@.@', '.@.@.@.@@@', '@.@@@.@@@@', '.@@@@@@@@.', '@.@.@@@.@.']

read_file = open("input.txt", "r")
lines = read_file.readlines()

grid = []

for line in lines:
    grid.append(line)


def countRolls(row, col, top, bottom, toponly, bottomonly):
    count = 0
    if grid[row][col-1] == '@':#left
        count += 1
    if grid[row][col+1] == '@': #right
        count += 1
    if toponly and grid[row+1][col] == '@': #down
        count += 1
    if bottomonly and grid[row-1][col] == '@': #up
        count += 1

    if not top and not bottom:
        if grid[row-1][col] == '@': #up
            count += 1
        if grid[row+1][col] == '@': #down
            count += 1
        if grid[row-1][col-1] == '@': #up left
            count += 1
        if grid[row+1][col-1] == '@': #down left
            count += 1
        if grid[row-1][col+1] == '@': #up right
            count += 1
        if grid[row+1][col+1] == '@': #down right
            count += 1
    return count

for row in range(len(grid)):
    for col in range(len(grid[row])):
        count = 0
        if i == 0:
            if grid[row][col] == '@' and (j == 0 or j == len(grid[row]) - 1): #first one or last
                if j == 0: #first one
                    #look at the three adjacent
                    if grid[row][col+1] == '@':
                        count += 1
                    if grid[row+1][col] == '@':
                        count += 1
                    if grid[row+1][col+1] == '@':
                        count += 1
                else: #last one
                    if grid[row][col-1] == '@':
                        count += 1
                    if grid[row+1][col] == '@':
                        count += 1
                    if grid[row+1][col-1] == '@':
                        count += 1
            else:
                if j == len(grid[row]) - 1 and grid[row][col] == '.':
                    continue #skip if last one is a .
                #all the others
                if grid[row][col] == '@':
                    count = countRolls(row, col, top=True, bottom=False, toponly=True, bottomonly=False)
                    # countRolls already counted down, just need to add diagonals
                    if grid[row+1][col-1] == '@':
                        count += 1
                    if grid[row+1][col+1] == '@':
                        count += 1
        elif i == len(grid) - 1: # last row
            if grid[row][col] == '@' and (j == 0 or j == len(grid[row]) - 1): #first one or last
                if j == 0:
                    if grid[row][col+1] == '@':
                        count += 1
                    if grid[row-1][col] == '@':
                        count += 1
                    if grid[row-1][col+1] == '@':
                        count += 1
                else:
                    if grid[row][col-1] == '@':
                        count += 1
                    if grid[row-1][col] == '@':
                        count += 1
                    if grid[row-1][col-1] == '@':
                        count += 1
            else:
                if j == len(grid[row]) - 1 and grid[row][col] == '.':
                    continue #skip if last one is a .
                #all the others
                if grid[row][col] == '@':
                    count = countRolls(row, col, top=False, bottom=True, toponly=False, bottomonly=True)
                    # countRolls already counted up, just need to add diagonals
                    if grid[row-1][col-1] == '@':
                        count += 1
                    if grid[row-1][col+1] == '@':
                        count += 1

        else: #MID
            if grid[row][col] == '@' and (j == 0 or j == len(grid[row]) - 1): #first one or last
                if j == 0:
                    if grid[row-1][col+1] == '@':
                        count += 1
                    if grid[row+1][col+1] == '@':
                        count += 1
                    if grid[row][col+1] == '@':
                        count += 1
                    if grid[row+1][col] == '@':
                        count += 1
                    if grid[row-1][col] == '@':
                        count += 1
                else:
                    if grid[row-1][col-1] == '@':
                        count += 1
                    if grid[row+1][col-1] == '@':
                        count += 1
                    if grid[row][col-1] == '@':
                        count += 1
                    if grid[row+1][col] == '@':
                        count += 1
                    if grid[row-1][col] == '@':
                        count += 1
            else: #MID
                if j == len(grid[row]) - 1 and grid[row][col] == '.':
                    continue #skip if last one is a .
                #all the others
                if grid[row][col] == '@':
                    count = countRolls(row, col, top=False, bottom=False, toponly=False, bottomonly=False)
        if grid[row][col] == '@' and count < 4:
            res += 1

        j += 1
    j = 0
    i += 1

print(res)

