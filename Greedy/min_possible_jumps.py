def jump1(a):
    endpoint=0
    farpoint=0
    count=0
    for i in range(len(a)-1):
        farpoint=max(farpoint,i+a[i])

        if i==endpoint:
            count+=1
            endpoint=farpoint
        if farpoint>len(a)-1:
            break
    return count

def jump(a):
    r=0
    c=0
    l=0
    flag=False
    while r<len(a)-1:
        m=0
        for i in range(l,r+1):
            if (i+a[i])>m:
                m=i+a[i]
            if m>len(a)-1:
                flag=True
        l=r+1
        r=m
        c+=1
        if flag:
            break
    return c

    
a=[3,4,3,2,5,4,3]
print(jump(a))