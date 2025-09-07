def value(l,d,t,i=0):
    if i==len(d):
        return "Invalid"
    if d[l[i]]==t:
        return d[l[i]]
    return value(l,d,t,i+1)
    
def find_d(a,t,i=0,d={}):
    if i==len(a):
        return value(list(d.keys()),d,t)
    if a[i] not in d:
        d[a[i]]=1
    else:
        d[a[i]]+=1
    return find_d(a,t,i+1,d)   
a=[2,4,3,3,2,6,1,2,3,6,6,5,6]
t=4
print(find_d(a,t))   