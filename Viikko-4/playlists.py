def count(t):
    # Convert the list to a set to remove duplicates
    unique_songs = set(t)
    # Calculate the number of unique subsets
    total = 2 ** len(unique_songs) - 1
    # Return the total number of unique playlists
    return total

if __name__ == "__main__":
    print(count([1,2,3,4])) # 15
    print(count([1,1,1,1])) # 1
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 15
    print(count([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) # 31