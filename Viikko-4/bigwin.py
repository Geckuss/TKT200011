def count(t):
    counts = {}
    total = 0
    for num in t:
        if num % 2 == 0:
            total += counts.get(num // 2, 0)
        counts[num] = counts.get(num, 0) + 1
    return total