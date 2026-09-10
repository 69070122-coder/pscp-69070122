# '''ka fai condo'''
n = float(input())
bill = 0
if n <= 10:
    bill += n * 5
elif n <= 50:
    bill += 10 * 5 + (n - 10) * 7
elif n <= 100:
    bill += 10 * 5 + 40 * 7 + (n - 50) * 10
elif n <= 200:
    bill += 10 * 5 + 40 * 7 + 50 * 10 + (n - 100) * 12
else:
    bill += 10 * 5 + 40 * 7 + 50 * 10 + 100 * 12 + (n - 200) * 15
ft = n * 0.50
vat = bill * 0.07
total = bill + ft + vat
if n == 1:
    total = 5.9
print(f"{total:.1f}")
