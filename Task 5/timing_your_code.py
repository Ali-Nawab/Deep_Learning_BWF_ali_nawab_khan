import time
import timeit
# Code to time
start_time = time.time()

i = 0
while i < 10000000:
    i += 1

end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.5f} seconds")





# Code to time
code_to_time = "for i in range(10000000): i+=1"
# ... Your code goes here ...

# Time the code
elapsed_time = timeit.timeit(code_to_time, number=1000)

print(f"Elapsed time: {elapsed_time:.5f} seconds")

