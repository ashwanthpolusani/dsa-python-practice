# Given an array.
# Find all subsets of that array

def subset(a,l=[],i=0):
   if i==len(a):
      print(l)
      return
   subset(a,l+[a[i]],i+1)
   subset(a,l,i+1)

a=[2,6,4]
print(subset(a))
