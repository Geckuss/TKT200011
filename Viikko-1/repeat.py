def find(s):
    n = len(s)
    
    # Käydään läpi kaikki mahdolliset toistettavien merkkijonojen pituudet
    for length in range(1, n + 1):
        if n % length == 0:
            repeated_string = s[:length] * (n // length)
            if repeated_string == s:
                return length

    # Jos merkkijonoa ei voi toistaa, palautetaan sen pituus
    return n

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
