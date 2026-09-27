n = int(input("Enter the number of elements: "))

arr = list(map(int, input("Enter the elements: ").split()))

# Precompute frequency
hash_table = [0] * 13

for i in range(n):
    hash_table[arr[i]] += 1

q = int(input("Enter the number of queries: "))

while q > 0:
    number = int(input("Enter the number to search: "))

    # Fetch frequency
    print("Frequency:", hash_table[number])

    q -= 1