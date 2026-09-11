count = {
    "Amit": 3,
    "Rahul": 3,
    "Sneha": 2
}
highest=0
employee=[]
for name,occurence in count.items():
    if occurence>highest:
        highest=occurence
        employee=[name]
    elif occurence==highest:
        employee.append(name)
print(employee)