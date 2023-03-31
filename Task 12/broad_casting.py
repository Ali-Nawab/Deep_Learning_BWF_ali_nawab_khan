import numpy as np

# Scenario 1

a1 = np.arange(8).reshape(2, 4)
a2 = np.arange(8, 16).reshape(2, 4)

print(a1)
print(a2)


print(a1 + a2)

# Scenario 2
a1 = np.arange(9).reshape(3, 3)
a2 = np.arange(3).reshape(1, 3) # small array will broadcast to large array.

print(a1, a2)

print(a1 + a2)


# if x = 1 and y = n then also operation will take place(same dimension).

a1 = np.arange(3).reshape(1, 3)
a2 = np.arange(12).reshape(4, 3)

print(a1, a2)

print(a1 + a2)


# if x = 1 and y != n then also operation will not take place.

a9 = np.arange(3).reshape(1, 3)
a10 = np.arange(16).reshape(4, 4)

# print(a9 + a10)

# if x = 1 and y = 1 then the operation will take place no matter what

a13 = np.arange(1).reshape(1, 1)
a14 = np.arange(20).reshape(4, 5)

print(a13 + a14)

# if they are of dfferent dimension then also operation will take place

a15 = np.arange(4)
a16 = np.arange(20).reshape(5, 4)

print(a15 + a16)


