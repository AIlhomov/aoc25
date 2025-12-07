read_file = open("input.txt", "r")
lines = read_file.readlines()

homework = []

for line in lines:
    homework.append(line.strip('\n'))

#print(homework)


resMultiply = 1
resAdd = 0
res = 0
i = 0

for op in homework[len(homework)-1]:
    if op == ' ':
        continue
    numbers = []
    if op == '*':
        for j in range(len(homework)-1):
            numbers = homework[j].split()
            num = numbers[i]
            resMultiply *= int(num)
        res += resMultiply
        resMultiply = 1
    elif op == '+':
        for j in range(len(homework)-1):
            numbers = homework[j].split()
            num = numbers[i]
            resAdd += int(num)
        res += resAdd
        resAdd = 0
    i += 1
print(res)