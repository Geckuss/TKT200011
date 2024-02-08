import time

n = 10**5

# Luo tyhjä lista
lst = []

# Aloita ajanotto
start_time = time.time()

# Lisää luvut listaan
for i in range(1, n+1):
    lst.append(i)

# Lopeta ajanotto ja tulosta kulunut aika
end_time = time.time()
print(f"Aikaa kului lisäämiseen: {end_time - start_time} sekuntia")

# Aloita ajanotto uudelleen
start_time = time.time()

# Poista luvut listasta
for _ in range(n):
    del lst[0]

# Lopeta ajanotto ja tulosta kulunut aika
end_time = time.time()
print(f"Aikaa kului poistamiseen: {end_time - start_time} sekuntia")