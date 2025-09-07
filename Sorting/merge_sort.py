# merge sort
def merge(l,r):
    c=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if l[i]>r[j]:
            c.append(r[j])
            j+=1
        else:
            c.append(l[i])
            i+=1
    while i<len(l):
        c.append(l[i])
        i+=1
    while j<len(r):
        c.append(r[j])
        j+=1
    return c
def merge_sort(x):
    if len(x)==1:
        return x
    m=len(x)//2
    l=merge_sort(x[:m])
    r=merge_sort(x[m:])
    return merge(l,r)
    
m=[2, 33, 4,0,99, 5, 5, 6, 8, 9, 9, 11, 12, 13]
print(merge_sort(m))