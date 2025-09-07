#check sum of subset of array

def subset(a,k,l=[],i=0):
    if k==0:
        print(l)
        return 
    if i==len(a):
        return 
    if a[i]>k:
        subset(a,k,l,i+1)
    subset(a,k-a[i],l+[a[i]],i+1)
a=[7,8,4]
k=10
subset(a,k)