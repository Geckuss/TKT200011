def find(t, k):
    if not t:
        return k - 1
    t.sort()
    if len(t) == 1:
        return max(t[0] - 1, k - t[0])
    max_distance = max((b - a) // 2 for a, b in zip(t, t[1:]))
    max_distance = max(max_distance, t[0] - 1, k - t[-1])
    return max_distance