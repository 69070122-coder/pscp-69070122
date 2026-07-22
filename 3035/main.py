'''this module is for checking if the eye are in the designated circle'''
r, x, y = map(int,input().split())
if (x)**2 + (y)**2 < (r)**2:
    print("IN")
elif x**2 + y**2 == r**2:
    print("ON")
else:
    print("OUT")
