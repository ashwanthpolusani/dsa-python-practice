ml = -1

def coins(a, t, l=[], i=0):
    global ml
    if t < 0:
        return
    if t == 0:
        if ml == -1:
            ml = len(l)
        else:
            ml = min(ml, len(l))
        return
    if i == len(a):
        return
    coins(a, t-a[i], l+[a[i]], i)    # use same coin again
    coins(a, t, l, i+1)               # skip current coin

# Test cases
a = [2, 4,6 ,8,10]
t = 8
coins(a, t)
print(ml)