def count(s):
    # Laske kaikki mahdolliset osajonot
    total = len(s) * (len(s) + 1) // 2

    # Alusta ryhmän pituus
    group_length = 0
    # Käy läpi merkkijono
    for i in range(len(s)):
        # Jos merkki on a, kasvata ryhmän pituutta
        if s[i] == 'a':
            group_length += 1
        else:
            # Muuten vähennä ryhmän tuottamat osajonot ja alusta ryhmän pituus
            total -= group_length * (group_length + 1) // 2
            group_length = 0
    # Vähennä viimeisen ryhmän tuottamat osajonot
    total -= group_length * (group_length + 1) // 2

    # Lisää osajonot, jotka päättyvät a-merkkiin
    total += group_length * (group_length + 1) // 2

    return total

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9
    print(count("wvlmmzxzjvaltdohf")) # 76