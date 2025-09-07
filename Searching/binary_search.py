# given a sorted array with duplicate elements and a key element
# check if the key exists in the list or not

def binary(a,k):
    l=0
    r=len(a)-1
    mid=0
    while l<=r:
        mid=(l+r)//2
        if a[mid]==k:
            # while mid<len(a)-1 and a[mid+1]==k:   for getting highest index of that element
            #     mid=mid+1
            return mid
        elif a[mid]>k:
            r=mid-1
        else:
            l=mid+1
    return -1

a=[2,3,5,6,7,7,8,9,10,10,10,13,15,15,15,15]
k=7
print(binary(a,k))