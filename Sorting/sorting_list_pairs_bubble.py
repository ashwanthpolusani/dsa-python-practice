def bubble(a):
    n=len(a)
    for i in range(n-1):
        flag=True
        for j in range(n-1-i):
            if a[j][1]>a[j+1][1]:
                a[j],a[j+1]=a[j+1],a[j]
                flag=False
        print(a)
        if flag:
            break
a=[[2,3],[5,1],[1,4],[2,7],[1,2]]
print(bubble(a))