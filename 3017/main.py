"""bai set"""
x = int(input())
sur_charge = (10*x)/100
if sur_charge >= 1000:
    sur_charge = 1000
elif sur_charge <= 50:
    sur_charge = 50
else:
    pass
vat = (7* (x + sur_charge))/ 100
print (f"{x + sur_charge + vat:.2f}")
