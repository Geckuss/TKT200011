def count(t):
    inversions = 0
    n = len(t)

    # Käydään läpi kaikki mahdolliset indeksiparit (i, j)
    for i in range(n):
        for j in range(i + 1, n):
            if t[i] > t[j]:
                inversions += 1

    return inversions

if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12
