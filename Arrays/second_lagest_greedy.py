# Given an array
# find the largest and second largest element in the array

numbers=[2,19,44,64,3,59,34,77,9,2,868,2,67,101,53]
def find_2nd_max(l):
    m=-float('inf')
    sm=0
    for i in l:
        if i>sm and i!=m:
            sm=i
        if i>m:
            sm=m
            m=i
    return m,sm
print(find_2nd_max(numbers))
