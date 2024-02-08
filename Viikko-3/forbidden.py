def count(s):
    # Alustetaan muuttujat
    total = 0
    consecutive_non_a = 0

    # Käydään läpi merkkijono
    for char in s:
        if char == 'a':
            # Jos merkki on 'a', lisätään osajonojen määrä kokonaismäärään
            total += (consecutive_non_a * (consecutive_non_a + 1)) // 2
            consecutive_non_a = 0
        else:
            # Jos merkki ei ole 'a', kasvatetaan osajonojen määrää
            consecutive_non_a += 1

    # Lisätään loput osajonot kokonaismäärään
    total += (consecutive_non_a * (consecutive_non_a + 1)) // 2

    return total

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9