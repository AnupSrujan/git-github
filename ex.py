def fib(index):
    sequence = [1, 1]
    sum = 0
    if (index == 1):
        return 1
    elif (index == 2):
        return 1
    else:
        for i in range(2, index):
            first_index = i - 1
            sec_index = i - 2
            sum = sequence[first_index] + sequence[sec_index]
            sequence.append(sum)
        return sequence[index - 1]
print(fib(1))
print(fib(7))












