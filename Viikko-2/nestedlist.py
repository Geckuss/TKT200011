def count(t):
    # Alusta laskuri
    counter = 0

    # Käy läpi lista
    for element in t:
        # Jos elementti on luku, lisää laskuriin yksi
        if isinstance(element, int):
            counter += 1
        # Jos elementti on lista, kutsu funktiota uudelleen kyseiselle listalle
        elif isinstance(element, list):
            counter += count(element)

    return counter

if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8