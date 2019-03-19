def binary_search(listdata, value):
    low = 0
    high = len(listdata)-1
    while(low<=high):
        mid = (low+high)//2
        #print(mid)
        if listdata[mid] == value:
            return mid
        elif listdata[mid]<value:
            low = mid + 1
        else:
            high = mid - 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
#print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))