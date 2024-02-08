def create(n):
    # Luo lista, jossa on vuorotellen parilliset ja parittomat luvut
    return [i for i in range(1, n+1, 2)] + [i for i in range(2, n+1, 2)]

if __name__ == "__main__":
    print(create(6)) # [1, 3, 5, 2, 4, 6]
    print(create(10)) # [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    print(create(15)) # [1, 3, 5, 7, 9, 11, 13, 15, 2, 4, 6, 8, 10, 12, 14]