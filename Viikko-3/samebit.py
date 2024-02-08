def count(s):
    # Laske kuinka monta kertaa kumpikin bitti esiintyy bittijonossa
    counts = [0, 0]
    for bit in s:
        counts[int(bit)] += 1

    # Laske kuinka monta tapaa on valita kaksi samaa bittiä
    return sum(count * (count - 1) // 2 for count in counts)

if __name__ == "__main__":
    print(count("0101")) # 2
    print(count("000000")) # 15
    print(count("000111")) # 6
    print(count("00100001101100")) # 46