s= "abc"
dict = {}
for i in s:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)
count = 0

value = min(i for i in dict.values())
print(value)

for j, v in dict.items():
    if v == value:
        count = 0
    else:
        count += 1

if count == 0:
    print("yes")
else:
    print('No')