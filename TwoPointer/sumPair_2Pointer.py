# Given a array and a target sum, find the pair of elements in the array whose sum is equal to the target sum.

def sumPair(a,target):
    i=0
    j=len(a)-1
    s=0
    while i<=j:
        if a[i]+a[j]==target:
            return "Found"
        if a[i]+a[j]>target:
            j-=1
        else:
            i+=1
    return "Not Found"
a=[2,7,11,15]
target=9
print(sumPair(a,target))