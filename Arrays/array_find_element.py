#given an array and a element k. find the number of occurrences of k in the array

# function to find frequency of a given number 
def findfreq(a,k,i=0):
    if i==len(a):
        return 0
    if a[i]==k:
        return 1+findfreq(a,k,i+1)
    else:
        return findfreq(a,k,i+1)

# function used for iteration just like a for loop
def findele(a,k,i=0,s=set()):
    if a[i] in s:
        return
    if i==len(a):
        return "Invalid Input"
    if findfreq(a,a[i])==k:
        return a[i]
    s.add(a[i])
    return findele(a,t,i+1)
    
    
a=[2,4,3,3,2,6,1,2,3,6,6,5,6]
t=4
print(findele(a,t))    
    