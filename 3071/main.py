'''จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r'''
A = int(input())
B = int(input())
Dih = int(input())
R = int(input())
count = 0
while A <= B:
    if A % Dih == R:
        count += 1
    else:
        pass
    A += 1
print(count)
