# given two sorted lists. try to sort them into a sigle sorted list

l1=[2,4,5,8,9]
l2=[3,5,6,9,11,12,13]

def mergeTwoArrays(a,b):
    c=[]
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]>b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            i+=1
    while i<len(a):
        c.append(a[i])
        i+=1
    while j<len(b):
        c.append(b[j])
        j+=1
    return(c)
print(mergeTwoArrays(l1,l2))