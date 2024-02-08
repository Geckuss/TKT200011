def find(t):
    # Initialize variables
    indices = {}
    max_distance = 0
    # Iterate over the list
    for i, num in enumerate(t):
        # If the number is in indices, update max_distance
        if num in indices:
            max_distance = max(max_distance, i - indices[num])
        else:
            # Store the first occurrence of the number
            indices[num] = i
    # Return the maximum distance
    return max_distance

if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4
    print(find([10, 7, 10, 8, 10])) # 4