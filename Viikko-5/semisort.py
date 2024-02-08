def solve(t):
    n = len(t)
    half = sorted(t)[n//2:]
    return sum(1 for i in range(n//2) if t[i] in half) + sum(1 for i in range(n//2, n) if t[i] in half)
