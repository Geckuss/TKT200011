def solve(t):
    n = len(t)
    result = []
    for _ in range(n):
        min_index = t.index(min(t))
        if min_index != 0:
            t[0], t[min_index] = t[min_index], t[0]
            result.append('SWAP')
        if min_index != 0 or len(result) == 0 or result[-1] != 'MOVE':
            result.append('MOVE')
        t.append(t.pop(0))
    return result[:-1]