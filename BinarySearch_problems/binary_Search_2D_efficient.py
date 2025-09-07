a=[[2,5,7,8],
   [9,15,20,22],
   [25,30,35,40],
   [45,50,55,60]]

def binary(a,k):
    l=0
    r=len(a)*len(a)-1
    while l<=r:
        mid =(l+r)//2
        if a[mid//len(a[0])][mid%len(a[0])]==k:
            return "Found"
        elif a[mid//len(a[0])][mid%len(a[0])]>k:
            r=mid-1
        else:
            l=mid+1
    return "Not Found"
print(binary(a,60))

