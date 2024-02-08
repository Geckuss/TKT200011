def count(a, b, c):
    max_candies = 0

    # Käydään läpi mahdolliset määrät nallekarkkeja (i) ja suklaakarkkeja (j)
    # Niin kauan kuin karkkeja pystyy ostamaan kokonaismäärä rahalla c
    for i in range(c // a + 1):
        for j in range(c // b + 1):
            if (i * a) + (j * b) <= c:
                # Lasketaan ostettavien karkkien määrä ja päivitetään max_candies tarvittaessa
                max_candies = max(max_candies, i + j)

    return max_candies

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4
