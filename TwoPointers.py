
numbers = [12, 24, 36, 48, 60, 72]
left=0
right=len(numbers)-1

if left<right:
    numbers[left], numbers[right]= numbers[right], numbers[left]
    left=left+1
    right=right-1
print(numbers)