def generate(n):
    count = 0
    current_number = 1

    while count < n:
        num_str = str(current_number)
        # Tarkista, onko luvun ensimmäinen ja viimeinen numero sama
        if num_str[0] == num_str[-1]:
            count += 1
        # Siirry seuraavaan lukuun riippumatta siitä, täyttikö se ehdon
        current_number += 1

    # Palauta viimeinen luku, joka täytti ehdon
    return current_number - 1


if __name__ == "__main__":
    print(generate(1))   # 1
    print(generate(2))   # 2
    print(generate(3))   # 3
    print(generate(10))  # 11
    print(generate(123)) # 1141
