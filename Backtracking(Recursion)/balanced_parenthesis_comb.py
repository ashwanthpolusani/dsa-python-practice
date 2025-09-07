def makebrackets(n,o=0,c=0,s=""):
    if o>n or c>o:
        return
    if len(s)==2*n:
        print(s)
        return
    makebrackets(n,o+1,c,s+'(')
    makebrackets(n,o,c+1,s+')')
    return
n=int(input("Enter the number brackets: "))
makebrackets(n)