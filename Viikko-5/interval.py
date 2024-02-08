def count(t):
    t.sort()
    count = 0
    last_counted = None
    for i in range(len(t)):
        if last_counted is None or t[i] > last_counted:
            count += 1
            last_counted = t[i]
    return count