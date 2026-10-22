# Linear Search 
# Time complexity: \(O(n)\) in the worst case, because we may check every element.
numbers = [7, 12, 18, 24, 31]
target=7
for i in range(len(numbers)):
    if numbers[i]==target:
        print("Found at index: ", i)
        break
else:
    print("Not found !")

