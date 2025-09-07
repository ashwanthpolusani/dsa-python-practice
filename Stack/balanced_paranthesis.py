s="(({})){"

def bal_paranthesis(exp):
    s=[]
    d={'}':'{',')':'(',']':'['}
    for i in exp:
        if i in d.values():
            s.append(i)
        elif s and i in d.keys() and s[-1]==d[i]:
            s.pop()
        else:
            return "Not balanced"
    return "balanced" if s==[] else "Not Balanced"
print(bal_paranthesis(s))