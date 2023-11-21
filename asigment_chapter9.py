N = int(input("Enter the size of the array: "))
DATA = []

# Input array elements
for i in range(N):
    element = int(input("Enter element: "))
    DATA.append(element)

K = 0
LOC = 0
MAX = DATA[0]

while K < N:
    if DATA[K] > MAX:
        MAX = DATA[K]
        LOC = K
    K += 1

print(f"Maximum element: {MAX}")
print(f"Location of maximum element: {LOC}")
