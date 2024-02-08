def find(t):
    counts = {}
    for num in t:
        counts[num] = counts.get(num, 0) + 1

    for num, count in counts.items():
        if count == 1:
            return num

if __name__ == "__main__":
    print(find([1,1,2,1])) # 2
    print(find([4,5,5])) # 4
    print(find([1,1,1,1,2])) # 2
    print(find([8,8,5,8,8])) # 5
    print(find([5, 5, 5, 5, 5, 2, 5, 5])) # 2
