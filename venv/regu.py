# Given string YYUTTTTTEEE
# Output : TEYU

strg = "YYUTTTTTEEE"

example_strg = " "
count = 0
for i in strg:
    if i not in example_strg:
        example_strg += i

print(''.join(sorted(example_strg)))
