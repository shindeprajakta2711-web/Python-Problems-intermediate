# Even and odd counts
numbers = [10, 15, 20, 25, 30, 35]
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(even_count)
print(odd_count)