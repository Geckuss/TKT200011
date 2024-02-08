def count(t):
    sums = {0: [-1]}
    total = curr_sum = 0
    for i, num in enumerate(t):
        curr_sum += num
        if curr_sum not in sums:
            sums[curr_sum] = []
        for j in sums[curr_sum]:
            if t[j] == num and j < i:
                total += 1
        sums[curr_sum].append(i)
    return total