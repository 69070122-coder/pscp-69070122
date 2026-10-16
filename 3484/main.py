'''main'''
n, p = input().split()
n = int(n)
p = float(p)

tiles = []
row_tiles = [0] * n
row_points = [0] * n
col_tiles = [0] * n
col_points = [0] * n

total_tiles = 0
total_points = 0

for i in range(n):
    row = list(map(int, input().split()))
    tiles.append(row)

    for j in range(n):
        if row[j] > 0:
            row_tiles[i] += 1
            col_tiles[j] += 1
            total_tiles += 1

        row_points[i] += row[j]
        col_points[j] += row[j]
        total_points += row[j]

for i in range(n):
    print(*tiles[i], row_tiles[i], row_points[i])

print(*col_tiles)
print(*col_points)
print(total_tiles, total_points, f"{total_points * p:.2f}")
