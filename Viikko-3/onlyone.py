def find(t):
    # Alusta luku nollaksi
    number = 0
    # Käy läpi lista
    for num in t:
        # Käytä XOR-operaatiota
        number ^= num
    # Palauta luku
    return number

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
    print(find([5, 5, 5, 5, 5, 2, 5, 5])) # 2