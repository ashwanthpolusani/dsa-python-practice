# Given a list of stings. Sort them in lexological order

def lexsort(a):
    n=len(a)
    for i in range(n):
        flag=True
        for j in range(n-1-i):
            k=0
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False
        if flag:
            break
    return a

def limitedlexsort(a):
    n=len(a)
    for i in range(n):
        flag=True
        for j in range(n-1-i):
            k=0
            if a[j][0]>a[j+1][0]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False
            elif a[j][0]==a[j+1][0] and a[j][1]>a[j+1][1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False

        if flag:
            break
    return a

a=["zebra","cet","camera","caesor","apple"]
print(limitedlexsort(a))