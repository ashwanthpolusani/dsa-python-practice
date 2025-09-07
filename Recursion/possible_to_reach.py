#given a 3 numbers . check whether if the 2nd and 3rd nums subtracted from 2st for n times and gives a remainder 1
g=float('inf')
def check_Possibility(n,a,b,c=0):
    global g
    if n<1:
        return False
    if n==1:
        g=min(g,c)
        return True
    return check_Possibility(n-a,a,b,c+1) or check_Possibility(n-b,a,b,c+1)

n,a,b=20,3,5
res=g if check_Possibility(n,a,b) else False
print(res)