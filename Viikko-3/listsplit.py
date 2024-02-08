def count(t):
    # Etsi pienin luku
    min_num = min(t)
    # Laske kuinka monta kertaa pienin luku esiintyy listan alussa ja lopussa
    start_count = t.index(min_num) + 1
    end_count = len(t) - t[::-1].index(min_num)
    # Jos pienin luku esiintyy myös listan keskellä, palauta 0
    if min_num in t[start_count:end_count-1]:
        return 0
    # Muuten palauta pienimmän luvun esiintymiskertojen tulo
    return start_count * (len(t) - end_count + 1)

if __name__ == "__main__":
    print(count([2,1,1,3])) # 1
    print(count([1,1,1,1])) # 3
    print(count([1,2,3,1,2,3])) # 3
    print(count([1,2,3,4,3,2,1])) # 6
    print(count([4,3,2,1,2,3,4])) # 0