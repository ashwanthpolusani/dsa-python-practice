# Given a array with sorted rows and columns, but not sorted overall, find the element k in the array.
# Input: 2D array, k
# Output: "Found" or "Not Found

a=[[2, 7, 6,  8],
   [5, 7, 9, 10],
   [8, 12,13,15],
   [20,23,26,28],
   [30,36,40,45]]


def binary(a,k):
    i=0
    j=len(a[0])-1
    while i<len(a) and j>=0:
        if a[i][j]==k:
            return "Found"
        elif a[i][j]>k:
            j-=1
        else:
            i+=1
    return "Not Found"
k=3
print(binary(a,k))