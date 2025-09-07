def build(n,k):
    count=0
    res=None
    def generate(path,o,c):
        nonlocal count,res
        if len(path)==2*n:
            count+=1
            if count==k:
                res=''.join(path)
        if o<n:
            path.append('(')
            generate(path,o+1,c)
            path.pop()
        if c<o:
            path.append(')')
            generate(path,o,c+1)
            path.pop()
    generate([],0,0)
    return res if res else "Invalid"
print(build(3,6))