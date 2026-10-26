# Bubble Sort
numbers = [5, 2, 8, 1, 3]
n = len(numbers)
for i in range(n):
    for j in range(n-1-i):
        if numbers[j]>numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)

# Bubble Sort : These sort is done by comparing each value with each other, till the length of seq.
# So because of these lenght , it helps to run the loop till all numbers are compared.
# Complexity: Average and worst case \(O(n^2)\). Bubble Sort is useful 
# for learning sorting logic, though it is inefficient for large datasets.
