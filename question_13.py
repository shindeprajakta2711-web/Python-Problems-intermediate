# # frequency count of the words:
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count = {}
# for word in words:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
# print(count)


# Printing the most occurrent name and the count 
words = ["python","java","python","sql","java","python","sql"]
count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
highest=0
result=""
for name, occurrence in count.items():
    if occurrence>highest:
        highest=occurrence
        result=name
print("most frequent name: ",result)
print("Frequency:", highest)