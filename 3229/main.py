'''online game'''
base = int(input())
bonus = int(input())
days = int(input())

# ตัวคูณ
if days > 3:
    multiplier = 1.5
else:
    multiplier = 1.0

# คำนวณคะแนนรวม
total = (base + bonus) * multiplier

# แปลงเป็นจำนวนเต็ม
total = int(total)

# รหัสอันดับ
if total >= 1500:
    rank = 5
elif total >= 1000:
    rank = 4
elif total >= 500:
    rank = 3
elif total >= 200:
    rank = 2
else:
    rank = 1

# รหัสสถานะพิเศษ
if rank == 5 and days >= 7:
    status = 99
elif rank == 4 and bonus > 300:
    status = 88
else:
    status = 0

print(total)
print(rank)
print(status)
