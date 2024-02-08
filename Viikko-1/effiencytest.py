import time
import random

# Toteutus 1
def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

# Toteutus 2
def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    # Luodaan lista 10^7 satunnaisella luvulla
    numbers = [random.randint(1, 100) for _ in range(10**7)]
    
    # Mittaa suoritusaika ensimmäiselle toteutukselle
    start_time = time.time()
    result_1 = count_even_1(numbers)
    end_time = time.time()
    print("Toteutus 1 suoritusaika:", end_time - start_time)

    # Mittaa suoritusaika toiselle toteutukselle
    start_time = time.time()
    result_2 = count_even_2(numbers)
    end_time = time.time()
    print("Toteutus 2 suoritusaika:", end_time - start_time)
