"""password gen 67"""
name = input()
surname = input()
age = input()
if len(name) >= 5 and len(surname) >=5:
    print(name[:2]+surname[-1]+age[-1])
else:
    print(name[:1]+age+surname[-1])
