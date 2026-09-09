sales = [
    ("Laptop", 50000),
    ("Mouse", 800),
    ("Laptop", 50000),
    ("Keyboard", 1500),
    ("Mouse", 800),
    ("Laptop", 50000)
]
count={}
for product, price in sales:
    if product in count:
        count[product]+=1
    else:
        count[product]=1
print(count)