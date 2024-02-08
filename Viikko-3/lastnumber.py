import heapq

def find(t):
    # Muuta lista minimikeoksi
    heapq.heapify(t)
    # Toista, kunnes keossa on vain yksi luku
    while len(t) > 1:
        # Poista kaksi pienintä lukua keosta ja lisää niiden summa vähennettynä yhdellä takaisin kekoon
        heapq.heappush(t, heapq.heappop(t) + heapq.heappop(t) - 1)
    # Palauta keon ainoa jäljellä oleva luku
    return t[0]

if __name__ == "__main__":
    print(find([1,2,3,4])) # 7
    print(find([1,1,1])) # 1
    print(find([5,1,1,7,9,1,2])) # 20