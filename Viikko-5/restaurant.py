def find(a, d):
    events = sorted([(t, 1) for t in a] + [(t, -1) for t in d])
    max_empty = 0
    customers = 0
    last_departure = None
    for t, event in events:
        customers += event
        if customers == 0:
            last_departure = t
        elif last_departure is not None:
            max_empty = max(max_empty, t - last_departure)
            last_departure = None
    return max_empty