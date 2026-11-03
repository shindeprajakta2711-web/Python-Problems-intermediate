# Fetching the number to reach the target by using enumerate function 
# Intermediate level
numbers = [3, 2, 4, 8, 7, 5]
target = 9
seen = {}
for i , sum in enumerate(numbers):  # Enumerate function enables to take index and key value 
# these gives the dict type format that is key : values pair answer
    required=target-sum # For reaching the target we need to substract the sum or number 
    if required in seen:
        print([seen[required], i])
        break
    seen[sum]=i 