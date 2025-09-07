# bubble sort by leaving k elements at start,end and sorting remaining elements
def bubble(a,k):
    n=len(a)
    if 2*k>=n:
        return a
    for i in range(n-1-(2*k)):
        flag=True
        for j in range(k,n-1-i-k):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False
        if flag:
            break
    return(a)
a=[88,89,90,91,92,0,101,102,5,7,8,9]
k=3
print(bubble(a,k))
