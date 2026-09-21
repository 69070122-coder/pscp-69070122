'''lil rabbit'''
text = input()
s = text.upper()
max_u = 0
for i in range(len(s)):
    if s[i] == "B":
        count = 0
        for j in range(i + 1, len(s)):
            if s[j] == "U":
                count += 1
            else:
                break
        if count > max_u:
            max_u = count
if max_u >= 2:
    print("Yes", max_u)
elif "B" in s:
    pos = s.index("B")
    print(text[:pos] + text[pos] + "U" * (len(text) - pos - 1))
else:
    result = ""
    for i in range(len(text)):
        result += "BUU"[i % 3]
    print(result)