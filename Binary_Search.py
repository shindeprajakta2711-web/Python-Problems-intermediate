numbers = [7, 12, 18, 24, 31, 36, 42]
target = 24
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
    
# Step	Left	Right	Mid	Middle value
# 1     0	    6	    3	 24
# Target found!
# Here we found the target immediately. If the target were 36, we'd first check 24, then move to the right half and find 36.
# Time complexity: \(O(\log n)\). Each step roughly halves the search area.