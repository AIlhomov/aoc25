def read_points(filename="input.txt"):
    points = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x, y = map(int, line.split(","))
            points.append((x, y))
    return points

def solve(points):
    n = len(points)
    max_area = 0

    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            # Must be opposite corners: both x and y differ
            if x1 == x2 or y1 == y2:
                continue

            width  = abs(x1 - x2) + 1
            height = abs(y1 - y2) + 1
            area = width * height

            if area > max_area:
                max_area = area

    return max_area

if __name__ == "__main__":
    pts = read_points()
    ans = solve(pts)
    print(ans)
