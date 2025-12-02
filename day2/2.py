read_file = open("input.txt", "r")
lines = read_file.readlines()
res = 0

def part1(i):
    s = str(i)

    if len(s) % 2 != 0:
        return False

    half = len(s) // 2
    if s[:half] == s[half:]:
        return i #return the number so its summed later
    else:
        return 0
def part2(i):
    s = str(i)
    l = len(s)

    for d in range(1, l // 2 + 1):
        if l % d != 0:
            continue #must divide length exactly

        rep = l // d
        if rep < 2:
            continue #must repeat atleast twice
        
        chunk = s[:d]
        if chunk * rep == s:
            return True
    return False

for line in lines:
    rang = line.split(',')

    for i in range(len(rang)):
        if rang[i] == '\n':
            continue
        from1, to = rang[i].split('-')
        
        for j in range(int(from1), int(to)+1):
            if part2(j):
                res += j
print(res)
read_file.close()

    