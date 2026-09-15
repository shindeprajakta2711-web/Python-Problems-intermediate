# frequency count of the words:
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
count = {}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)