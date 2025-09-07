# Given a 2d array and a key, find the key in the array using binary search
# The 2d array is sorted row wise and column wise
# Logic: We are using binary search on the first column and then on the rows
def binary(arr,k):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==k:
            return "Found"
        elif arr[mid]>k:
            r=mid-1
        else:
            l=mid+1
    return "Not Found"

def bs2d(a,k):
    s=0
    e=len(a)-1
    while s<=e:
        m=(s+e)//2
        if (m<len(a)-1 and a[m][0]<=k and a[m+1][0]>k) or (m==len(a)-1 and a[m][0]<=k) :
            return binary(a[m],k)
        elif a[m][0]>k :
            e=m-1
        else:
            s=m+1
    return "Not Foundd"


a=[[1,2,3,4],
   [5,6,7,8],
   [9,10,11,12],
   [13,14,15,16]]
k=9
print(bs2d(a,k))