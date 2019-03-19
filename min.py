ex_array =  [1,12,2,53,23,6,17]





max_value = -99999999999999999999
min_value = 999999999999999999999
for i in ex_array:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print(max_value)
print(min_value)