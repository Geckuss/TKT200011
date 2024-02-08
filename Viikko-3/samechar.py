def count(s):
    # Alusta laskuri ja ryhmän pituus
    total = group_length = 0
    # Käy läpi merkkijono
    for i in range(len(s)):
        # Jos merkki on sama kuin edellinen, kasvata ryhmän pituutta
        if i > 0 and s[i] == s[i-1]:
            group_length += 1
        else:
            # Muuten laske ryhmän tuottamat osajonot ja alusta ryhmän pituus
            total += group_length * (group_length + 1) // 2
            group_length = 1
    # Lisää viimeisen ryhmän tuottamat osajonot
    total += group_length * (group_length + 1) // 2
    return total

if __name__ == "__main__":
    print(count("abc")) # 3
    print(count("aaa")) # 6
    print(count("aabba")) # 7
    print(count("ababab")) # 6