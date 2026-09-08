# Fetching the number to reach the target by using enumerate functions
numbers = [3, 2, 4, 8, 7, 5]
target = 9
seen = {}
for i , sum in enumerate(numbers):
    required=target-sum
    if required in seen:
        print([seen[required], i])
        break
    seen[sum]=i 