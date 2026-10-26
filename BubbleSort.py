# Bubble Sort
numbers = [5, 2, 8, 1, 3]
n = len(numbers)
for i in range(n):
    for j in range(n-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)

# Complexity: Average and worst case \(O(n^2)\). Bubble Sort is useful 
# for learning sorting logic, though it is inefficient for large datasets.
#