# Fetching the number to reach the target by using enumerate function 
numbers = [3, 2, 4, 8, 7, 5]
target = 9
seen = {}
for i , sum in enumerate(numbers):  # Enumerate function enables to take index and key value 
# these gives the dict type format without the use of the loop to run 
    required=target-sum
    if required in seen:
        print([seen[required], i])
        break
    seen[sum]=i 