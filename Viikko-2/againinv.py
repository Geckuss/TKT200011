def create(n, k):
    # Luo lista luvuista 1, 2, ..., n
    arr = list(range(1, n+1))

    for i in range(n, 0, -1):
        # Jos k on suurempi tai yhtä suuri kuin i-1, käännä osa listasta
        if k >= i-1:
            j = min(k, n-1)
            # Käännä osa listasta
            arr = arr[:i-1] + arr[i-1:j+1][::-1] + arr[j+1:]
            k -= j - i + 1

    return arr

if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(10, 34)) # esim. [1, 2, 3, 4, 5, 6, 10, 9, 8, 7]