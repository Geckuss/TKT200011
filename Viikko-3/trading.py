from collections import deque

def find(t):
    # Initialize variables
    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0
    queue = deque()

    # Iterate over prices
    for price in t:
        # Update variables
        buy1 = max(buy1, -price)
        sell1 = max(sell1, price + buy1)
        # Dequeue prices until we find a price where selling the stock would not result in a higher profit than sell1
        while queue and queue[0][1] < sell1:
            queue.popleft()
        # Enqueue the current price and the maximum profit that can be made by selling the stock at this price
        queue.append((price, sell1))
        # Update buy2 and sell2
        buy2 = max(buy2, queue[0][1] - price)
        sell2 = max(sell2, price + buy2)

    # Return the maximum possible profit
    return sell2

if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10
    print(find([4,3,1,3,5,1,4])) # 5
    print(find([5,3,5,5,2,3,4,3,3,4])) # 4