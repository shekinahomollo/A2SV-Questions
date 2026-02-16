matrix = []

for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            r = i + 1
            c = j + 1

# Manhattan distance to the center (3, 3)
moves = abs(r - 3) + abs(c - 3)

print(moves)