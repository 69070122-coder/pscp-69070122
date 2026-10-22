'''main'''
text = input()
result = ""

for ch in text:
    if text.count(ch) % 2 == 1 and ch not in result:
        result += ch

if result:
    print(result)
else:
    print("fully paired")
