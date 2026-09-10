'''hotel'''
n = input().strip()

d1 = int(n[0])
d2 = int(n[1])
d3 = int(n[2])
d4 = int(n[3])
d5 = int(n[4])

# หลักแรก: ชั้น
if d1 > 5:
    first = 9
elif d2 > 5:
    first = 10
elif d3 > 5:
    first = 11
elif d4 > 5:
    first = 12
elif d5 > 5:
    first = 14
else:
    first = 13

# ตรวจ Palindrome
palindrome = n == n[::-1]

# หลักที่สอง
if palindrome:
    if d1 + d5 > 5:
        second = 1
    elif d2 * d4 > 5:
        second = 2
    else:
        second = 0
else:
    if d5 != 0 and d1 // d5 > 5:
        second = 1
    elif d2 - d5 > 5:
        second = 2
    else:
        second = 0

# หลักที่สาม
total = d1 + d2 + d3 + d4 + d5
product = d1 * d2 * d3 * d4 * d5

if total > 25:
    third = 1
elif product > 55:
    third = 2
else:
    third = 0

print(f"{first}{second}{third}")
