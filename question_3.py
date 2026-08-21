# Frequency of the numbers occured in the list
numbers = [4, 7, 4, 2, 7, 9, 4, 2]
freq= {}
for i in numbers:
    if i in freq:
        freq[i]=freq[i]+1
    else:
        freq[i]=1
print(freq)