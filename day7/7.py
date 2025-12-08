def count_splits(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Find starting position S
    sr = sc = None
    for r in range(rows):
        c = grid[r].find('S')
        if c != -1:
            sr, sc = r, c
            break

    if sr is None:
        raise ValueError("No starting point 'S' found in the grid")

    beams = {(sr + 1, sc)}  # start just below S
    used_splitters = set()
    splits = 0

    while beams:
        new_beams = set()

        for (r, c) in beams:
            if not (0 <= r < rows and 0 <= c < cols):
                continue

            cell = grid[r][c]

            if cell == '.' or cell == 'S':
                # Beam just continues downward
                nr, nc = r + 1, c
                if nr < rows:
                    new_beams.add((nr, nc))

            elif cell == '^':
                if (r, c) not in used_splitters:
                    used_splitters.add((r, c))
                    splits += 1

                    nr = r + 1
                    if nr < rows:
                        # Down-left
                        if c - 1 >= 0:
                            new_beams.add((nr, c - 1))
                        # Down-right
                        if c + 1 < cols:
                            new_beams.add((nr, c + 1))

        beams = new_beams

    return splits


if __name__ == "__main__":

    read_file = open("input.txt", "r")
    lines = read_file.readlines()

    grid = []

    for line in lines:
        grid.append(line.strip('\n'))


    print(count_splits(grid))
