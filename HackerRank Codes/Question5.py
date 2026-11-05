# We have seen the applications of union, intersection, difference and 
# symmetric difference operations, but these operations do not make any changes or 
# mutations to the set.

# We can use the following operations to create mutations to a set:
# intersection_update	Keep {1,2,3,4,5,6,7,8,9,11}
# update	Add 55, 66
# symmetric_difference_update	Remove common 7; add 22,35,62,58
# difference_update	Remove 11,22,35,55,58,62,66

n = int(input())

A = set(map(int, input().split()))

N = int(input())

for i in range(N):

    operation, length = input().split()

    other_set = set(map(int, input().split()))

    if operation == "intersection_update":
        A.intersection_update(other_set)

    elif operation == "update":
        A.update(other_set)

    elif operation == "symmetric_difference_update":
        A.symmetric_difference_update(other_set)

    elif operation == "difference_update":
        A.difference_update(other_set)

print(sum(A))