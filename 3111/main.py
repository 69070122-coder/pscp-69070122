'''school cafeteria'''
from decimal import Decimal, ROUND_HALF_UP

member = input()
glocer = []
for _ in range(int(input())):
    price = Decimal(input())
    glocer.append(price)

total = sum(glocer)
if member == "Y":
    FINALE = total * Decimal("0.95")
elif total >= 500:
    FINALE = total * Decimal("0.97")
else:
    FINALE = total

FINALE = FINALE.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(FINALE)
