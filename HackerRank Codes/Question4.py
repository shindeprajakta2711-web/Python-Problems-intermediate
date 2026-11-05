# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

my_list=[]
n=int(input())

for i in range(n):
    command=input().split()
    
    if command[0]=="insert":
        my_list.insert(int(command[1]), int(command[2]))
    elif command[0]=="print":
        print(my_list)
    elif command[0]=="remove":
        my_list.remove(int(command[1]))
    elif command[0]=="append":
        my_list.append(int(commad[1]))
    elif command[0]=="sort":
        my_list.sort()
    elif command[0]=="pop":
        my_list.pop()
        
    elif command[0]=="reverse":
        my_list.reverse()
        
# Hash value 
n=int(input())
numbers=map(int(input().split()))
t=tuple(numbers)
print(hash(t))

#Polynomial Question
import numpy
p=numpy.array(int(input().split(), float))
x=float(input())
print(numpy.polyval(p,x))

#Determinant Question
Num=int(input())
matrix=[]
for i in range(Num):
    row=list(map(input().split()))
    matrix.append(row)
result=numpy.linalg.det(matrix)
print(result)