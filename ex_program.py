# ex_string = "hello world"
#
# ls = {}
#
# for i in ex_string:
#     if i not in ls:
#         ls[i] = 1
#     else:
#         ls[i] += 1
#
#
# print(ls)
#
#
#
# def fib(num):
#     count = 0
#     n0 = 1
#     n1 = 1
#     if num == 0:
#         return 1
#     elif num ==1:
#         return n1
#     else:
#         while count <= num:
#             n = n0 + n1
#             n0 = n1
#             n1 = n
#             count += 1
#             print(n)
#         return n
#
# print(fib(10))

#
# list1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#
# ex = []
#
#
# for i in list1:
#     if i not in ex:
#         ex.append(i)
#         if ex.count(i) > 1:
#             ex.remove(i)
#
#
# print(ex)
# st = ""
# for i in range(1, 10):
#     for j in range(i):
#
#         st += str(i)
# print(st)

# import os
# path = "C:/"
#
# for file in os.listdir(path):
#     print(file)
#     if os.path.isdir(file):
#         if file == 'Mongodb':
#             print("True")






ex_dict =                    {
                                "glossary": {
                                    "title": "example glossary",
                                    "GlossDiv": {
                                        "title": "S",
                                        "GlossList": {
                                            "GlossEntry": {
                                                "ID": "SGML",
                                                "SortAs": "SGML",
                                                "GlossTerm": "Standard Generalized Markup Language",
                                                "Acronym": "SGML",
                                                "Abbrev": "ISO 8879:1986",
                                                "GlossDef": {
                                                    "para": "A meta-markup language, used to create markup languages such as DocBook.",
                                                    "GlossSeeAlso": ["GML", "XML"]
                                                },
                                                "GlossSee": "markup"
                                            }
                                        }
                                    }
                                }
                           }
# for i, v in ex_dict.items():
#     for k, j in v.items():
#         if k == "title":
#
#             print(ex_dict[i][k])

# import json
#
# x = json.dump(ex_dict)
#
# example = {
#     'id1':  {'name': 'jay','age':22,},
#     'id2': {'name': 'salman','age': 52,},
#     'id3': {'name':'Ranveer','age' :26,},
#     'id4': {'name': 'jay', 'age': 22,},
# }
# for item in example:
#     for value in example:
#         if example[item] ==example[value]:
#             if item != value:
#                  key = value
#                  del example[key]
# print("example",example)
# ls = [{'a': 123, 'b': 1234},
#         {'a': 3222, 'b': 1234},
#         {'a': 123, 'b': 1234}]
# st = []
# for i in ls:
#     if i not in st:
#         st.append(i)
#         if st.count(i) > 1:
#             st.remove(i)
# print(st)


ls = [51, 51, 3, 4, 4]
ls = [51, 51, 3, 4, 4, 4, 51]
st = []
count = 0
for i in range(len(ls)):
    for j in ls:
        if ls[i] == j:
            count += 1
    if count > 1:
        count = 0
    else:
        st.append(ls[i])

print(st)

































































