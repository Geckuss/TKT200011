def count(s, k):
    visited = set()
    x, y = 0, 0
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for _ in range(k):
        for move in s:
            visited.add((x, y))
            dx, dy = moves[move]
            x, y = x + dx, y + dy
    visited.add((x, y))
    return len(visited)