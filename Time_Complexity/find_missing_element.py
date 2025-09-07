# find the missing element form the array
# the sorted array has all elements doulble times but 1 element is repeated single time

#time complexity: O(n/2)
def slide(l):
    for i in range(0,len(l)-1,2):
        if  l[i]!=l[i+1]:
            return l[i]
    return l[-1]

def divcon(l):
    m=len(l)//2
    if m==0 or m==len(l):
        return l[m]
    if l[m-1]==l[m] and (m+1)%2==0:
        divcon(l[m+1:])
    else:
        divcon(l[:m])
l=[2,2,4,4,6,6,7,8,8,9,9]
print(slide(l))
print(divcon(l))
