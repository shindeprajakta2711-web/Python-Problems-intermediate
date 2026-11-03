# Cummulative sum 
sales = [200, 100, 300, 150]
total=0
result=[]
for value in sales:
    total=total+value
    result.append(total)
print(result)