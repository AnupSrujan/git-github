ex_string = "abcdefghijklmnopqrstuvwxyz"

def strng_function(ex_string):

    strng = ""
    for i in ex_string[0:len(ex_string):2]:
        strng += i
    for j in ex_string[1:len(ex_string):2]:
        strng += j

    return strng

print(strng_function(ex_string))