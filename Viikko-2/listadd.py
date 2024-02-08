def create(t, x):
    # Luo uusi lista, jossa jokaiseen alkioon on lisätty luku x
    return [i + x for i in t]

if __name__ == "__main__":
    print(create([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]