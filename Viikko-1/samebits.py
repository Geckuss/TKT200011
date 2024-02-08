def count(s):
    count_zeroes = s.count('0')
    count_ones = len(s) - count_zeroes
    return min(count_zeroes, count_ones)

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
