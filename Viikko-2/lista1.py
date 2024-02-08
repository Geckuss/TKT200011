import time

n = 10**5

# Initialize the list
lst = []

# Start the timer
start_time = time.time()

# Add numbers to the list
for i in range(1, n+1):
    lst.append(i)

# Stop the timer and print the elapsed time
end_time = time.time()
print(f"Time to add elements: {end_time - start_time} seconds")

# Start the timer again
start_time = time.time()

# Remove numbers from the list
for _ in range(n):
    lst.pop()

# Stop the timer and print the elapsed time
end_time = time.time()
print(f"Time to remove elements: {end_time - start_time} seconds")