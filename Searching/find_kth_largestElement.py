# given an array. find the kth largest element without sorting and without considering duplicates.
# Note: Use this algorithm if max value <length of the array else use merge sort



#without duplicates
def find_kth_largest(arr,k):
    m=max(arr)
    a=[0]*(m+1)
    for i in range(len(arr)):
        a[arr[i]]=1
    print(a)
    for i in range(len(a)-1,-1,-1):
        if a[i]==1:
            k-=1
        if k==0:
            return i
    return "mak K doesn't Exist"

#with Duplicates
def find_kth_largest_withDup(arr,k):
    m=max(arr)
    a=[0]*(m+1)
    for i in range(len(arr)):
        a[arr[i]]+=1
    print(a)
    for i in range(len(a)-1,-1,-1):
        if a[i]>0:
            k-=a[i]
        if k<=0:
            return i
    return "mak K doesn't Exist"
arr=[2,13,4,2,9,9,3,5,8,7,13,3]
print(find_kth_largest(arr,3))
print(find_kth_largest_withDup(arr,3))
            