numbers = [7, 12, 18, 24, 31, 36, 42]
target = 36
left=0
right= len(numbers)-1
while left<=right:
    mid =(left+right)//2
    if numbers[mid]==target:
        print("Found at index: ", mid)
        break
    elif numbers[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print("Not Found")