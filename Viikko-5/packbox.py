def solve(t, x):
    t.sort()
    count = 0
    total_weight = 0
    for weight in t:
        if total_weight + weight <= x:
            total_weight += weight
            count += 1
        else:
            break
    return count