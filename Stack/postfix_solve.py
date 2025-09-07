a="15,-3,+,6,2,-,*"
l=a.split(',')
def solve_postfix(exp):
    s=[]
    for i in exp:
        if i[-1].isdigit():
            s.append(int(i))
        else:
            d=int(s.pop())
            b=int(s.pop())
            if i=='+':
                c=b+d
            elif i=='-':
                c=b-d
            elif i=='*':
                c=b*d
            elif i=='/':
                c=b//d
            s.append(c)
    return s[-1]


print(solve_postfix(l))
            

