# Given a list, k
# find the longest subarray with sum<=k

# Time Complexity O(2n)
def subarray1(a,k):
    m=0
    for i in range(len(a)):
        j=i
        s=0
        while j<len(a):
            j+=1
            if s+a[j-1]<=k:
                s+=a[j-1]
            else:
                j-=1
                break
        m=max(m,j-i)
    return m

# Time Complexity O(n)
def subarray(a,k):
    l=0
    r=0
    m=0
    s=0
    while r<len(a):
        s+=a[r]
        if s>k:
            l+=1
            s-=a[l-1]
        m=max(m,r-l+1)
        r+=1
    return m

a=[1,1,2,4,2,3,1,2,4,2,6,7,3,1,1,1]
k=6
print(subarray(a,k))