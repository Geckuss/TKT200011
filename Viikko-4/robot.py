def count(s):
    # Alusta muuttujat
    position = (0, 0)
    visited = {position}
    # Määritä liikkeet
    moves = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    # Käy läpi liikesarja
    for move in s:
        # Päivitä sijainti
        dx, dy = moves[move]
        position = (position[0] + dx, position[1] + dy)
        # Lisää sijainti vierailluihin ruutuihin
        visited.add(position)
    # Palauta vieraillut ruudut
    return len(visited)

if __name__ == "__main__":
    print(count("LL")) # 3
    print(count("UUDLRR")) # 5
    print(count("UDUDUDU")) # 2