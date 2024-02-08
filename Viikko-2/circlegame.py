def create(n):
    # Luo lista, jossa on luvut 1, 2, ..., n
    players = list(range(1, n+1))

    # Luo tyhjä lista, johon tallennetaan poistuvien leikkijöiden järjestys
    result = []

    # Aloita indeksi -1:stä, koska ensimmäinen poistettava leikkijä on toinen leikkijä
    index = -1

    while players:
        # Lisää indeksiin 1 (siirry seuraavaan leikkijään)
        index += 1

        # Jos indeksi on suurempi kuin leikkijöiden määrä, aloita alusta
        if index >= len(players):
            index = 0

        # Poista leikkijä ja lisää hänet tuloksena olevaan listaan
        result.append(players.pop(index))

    result.reverse()
    
    return result

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    print(create(4)) # [2,4,3,1]
    print(create(2)) # [2,1]