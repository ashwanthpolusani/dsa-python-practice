#find the length of longest sub sequence of numbers
def find1(l):
    stack=[]
    c=0
    for i in l:
        if stack and stack[-1]<i:
            stack.append(i)
        else:
            stack=[i]
        c=max(c,len(stack))
    return c

def find(l):
    maxlen=1
    c=0
    for i in range(len(l)-1):
        if l[i]+1 == l[i+1]:
            c+=1
        else:
            if c>maxlen:
                maxlen=c
            c=1
    if c>maxlen:
        maxlen=c
    return maxlen
        

l=[2,3,4,6,7,8,9,1,2,3,4,5,6,7,3,4,5,10,9]
print(find(l))
l=[1,2,3,2,3,4,5,6,7,8,9]
print(find(l))