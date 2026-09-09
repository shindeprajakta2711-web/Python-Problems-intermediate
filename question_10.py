# sales = [
#     ("Laptop", 50000),
#     ("Mouse", 800),
#     ("Laptop", 50000),
#     ("Keyboard", 1500),
#     ("Mouse", 800),
#     ("Laptop", 50000)
# ]
# count={}
# for product, price in sales:
#     if product in count:
#         count[product]+=1
#     else:
#         count[product]=1
# print(count)


# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count={}
# for fruits in words:
#     if fruits in count:
#         count[fruits]+=1
#     else:
#         count[fruits]=1
# print(count)


attendance = [
    "Amit",
    "Rahul",
    "Amit",
    "Sneha",
    "Rahul",
    "Amit",
    "Sneha"
]
count ={}
for name in attendance:
    if name in count:
        count[name]+=1
    else:
        count[name]=1
highest=0
name = ""
for name ,occurence in count.items():
    if occurence>highest:
        highest=occurence
        employee=name
print(employee)
print(highest)