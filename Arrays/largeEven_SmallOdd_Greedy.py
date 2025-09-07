def find(a,l=[-float('inf'),float('inf')]):
    for i in a:
        if i%2==0 and i>l[0]:
            l[0]=i
        elif i%2==1 and i<l[1]:
            l[1]=i
    return l
a=[2,3,34,345,546,234,52,236,56,54,34,6,547,34,7,9]
print(find(a))


print(max([a[i] for i in range(0,len(a),2)]))