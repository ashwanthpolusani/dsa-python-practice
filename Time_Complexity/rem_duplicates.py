def elope(l):
    d={}
    for i in l:
        if i not in d:
            d[i]=0
    return list(d.keys())
if __name__=='__main__':
    l=[8,2,3,4,3,3,4,5,6,7,9,2,4]
    print(elope(l))