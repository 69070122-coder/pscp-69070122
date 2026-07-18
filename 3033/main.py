'''this module is for calculate the lenght and height of the paper
that needed for wraping the cookie package'''
rasmee,suung,rayakoa = list(map(float, input().split()))
PI = 3.14
circum = (2*PI*rasmee) + rayakoa
hight = suung + 2*(rasmee)
long = circum
print(f"{hight:.2f} {long:.2f}")
