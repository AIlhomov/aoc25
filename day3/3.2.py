read_file = open("input.txt", "r")
lines = read_file.readlines()

res = 0

for line in lines:
    allValsinLine = []
    addThis = 0
    for digit in line:
        if digit == '\n':
            continue
        digit = int(digit)
        allValsinLine.append(digit)
    pick = 12 # 12 integers possible ONLY
    chosenDigits = []
    start = 0

    while pick > 0:
        end = len(allValsinLine) - pick
        bestDigit = -1
        bestIndex = -1

        for i in range(start, end + 1):
            if allValsinLine[i] > bestDigit:
                bestDigit = allValsinLine[i]
                bestIndex = i
        chosenDigits.append(str(bestDigit))
        start = bestIndex + 1
        pick -= 1
    val = int(''.join(chosenDigits))
    res += val
print(res)