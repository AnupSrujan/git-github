def fib(n):
    sequence = [1,1]
    sum = 0
    if n == 1:
        return 1
    elif n==2:
        return 1
    else:
        for i in range(2, n):
            first_index = i - 1
            sec_index = i - 2
            sum = sequence[first_index] + sequence[sec_index]
            sequence.append(sum)
        return sequence[n - 1]
print(fib(7))
