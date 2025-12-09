#!/usr/bin/env python3
import sys

def parse_points(lines):
    pts = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        x, y, z = map(int, line.split(","))
        pts.append((x, y, z))
    return pts

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def main():
    lines = sys.stdin.read().strip().splitlines()
    pts = parse_points(lines)
    n = len(pts)
    if n < 2:
        print("0")
        return

    # Build all edges: (dist2, i, j)
    edges = []
    for i in range(n):
        x1, y1, z1 = pts[i]
        for j in range(i + 1, n):
            x2, y2, z2 = pts[j]
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx*dx + dy*dy + dz*dz
            edges.append((d2, i, j))

    # Sort by distance (ascending)
    edges.sort(key=lambda e: e[0])

    dsu = DSU(n)
    components = n
    last_i = last_j = None

    # Kruskal: keep adding edges that connect different components
    for _, i, j in edges:
        if dsu.union(i, j):
            components -= 1
            last_i, last_j = i, j
            if components == 1:
                break

    # Multiply X coordinates of the last two junction boxes that were connected
    x1 = pts[last_i][0]
    x2 = pts[last_j][0]
    print(x1 * x2)

if __name__ == "__main__":
    main()
