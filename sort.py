ex_array = [1,2,4,9,14,81,100]
integer = 5
def insertion_integer(ex_array, integer):
    array = []

    if integer < ex_array[0]:
        array.append(integer)
        array += ex_array

    elif integer > ex_array[-1]:
        array += ex_array
        array.append(integer)

    else:
        for i in range(len(ex_array)):
            array.append(ex_array[i])
            if integer < ex_array[i+1] and integer > ex_array[i]:
                array.append(integer)
                array += (ex_array[i+1:])
                break
    return array


print(insertion_integer(ex_array, integer))



