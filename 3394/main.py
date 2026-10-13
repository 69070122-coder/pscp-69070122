'''main'''
n, s = input().split()
n = int(n)
s = int(s)

students = []

for _ in range(n):
    students.append(int(input()))

visited = []
count = 0
current = s

while current and current not in visited:
    visited.append(current)
    count += 1
    current = students[current - 1]

print(count)
