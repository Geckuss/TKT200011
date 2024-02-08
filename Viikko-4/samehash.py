def find(N):
    if N == 1:
        return ('0', '1')
    hash_table = {}
    for i in range(N * N):
        s = str(i)
        h = hash(s) % N
        if h in hash_table:
            return (hash_table[h], s)
        else:
            hash_table[h] = s