dial_start = 50

read_file = open("input.txt", "r")
lines = read_file.readlines()
res = 0

for line in lines:
    direction = line[0]
    distance = int(line[1:].strip())

    if direction == 'R':
        #hit 0 at clicks: (100-pos), (100-pos)+100, (100-pos)+200, ...
        if dial_start == 0:
            res += distance // 100
        else:
            first_zero = 100 - dial_start
            if distance >= first_zero:
                res += ((distance - first_zero) // 100) + 1
        dial_start = (dial_start + distance) % 100
    else:
        #hit 0 at clicks: pos, pos+100, pos+200, ...
        if dial_start == 0:
            res += distance // 100
        else:
            if distance >= dial_start:
                res += ((distance - dial_start) // 100) + 1
        dial_start = (dial_start - distance) % 100
print(res)
read_file.close()

