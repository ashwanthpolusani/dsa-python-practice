sub=[4,1,2]
s=[2,1,3,4]
def find(sub,s):
    res=[]
    for i in sub:
        a=-1
        flag=False
        for j in s:
            if i==j:
                flag=True
            if flag:
                if j>i:
                    a=j
                    break
        res.append(a)
    return res
def find1(sub,s):
    res=[-1]*len(sub)
    d={}
    st=[]
    for i in range(len(sub)):
        d[sub[i]]=i
    for i in s:
        while st and st[-1]<i:
            res[d[st.pop()]]=i
        if i in d :
            st.append(i)
    return res
print(find(sub,s))
print(find1(sub,s))