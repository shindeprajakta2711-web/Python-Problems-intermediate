# numbers = [7, 12, 18, 24, 31]
# target=12
# for i in range(len(numbers)):
#     if numbers[i]==target:
#         print("Found at index: ", i)
#         break
# else:
#     print("Not found !")
numbers = [7, 12, 18, 24, 31]
target = 12

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not found")