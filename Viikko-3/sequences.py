def count(s):
    # Alusta laskurit
    t_count = i_count = r_count = a_count = 0
    # Käy läpi merkkijono
    for char in s:
        # Kasvata laskureita
        if char == 't':
            t_count += 1
        elif char == 'i':
            i_count += t_count
        elif char == 'r':
            r_count += i_count
        elif char == 'a':
            a_count += r_count
    # Palauta 'a'-laskurin arvo
    return a_count

if __name__ == "__main__":
    print(count("aybabtu")) # 0
    print(count("tira")) # 1
    print(count("ritari")) # 6
    print(count("tiratiratira")) # 45
    print(count("xaxrxixtx")) # 4