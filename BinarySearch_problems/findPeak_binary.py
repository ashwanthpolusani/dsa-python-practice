# Find the peak element in an array
# Peak element is the element which is greater than its neighbours
# If there are multiple peak elements, return the first one
# If there is no peak element, return -1
# Time complexity: O(logn)
# Space complexity: O(1)
# Binary search approach
# If the middle element is greater than its neighbours, it is the peak element
# If the middle element is less than its left neighbour, the peak element is in the left half
# If the middle element is less than its right neighbour, the peak element is in the right half
# If the middle element is equal to its neighbours, the peak element maybe in the left or right half
# If the middle element is equal to its neighbours, we can move to the left or right half and continue the search


# Example: [5,2,4,6,7,8,6,5,4,6,7,8,8,6,5,4,7]
# Peak element: 8
a=[5,6,7,8,9,10,11,11,10,3,9,8]
def findPeak(a):
    l=0
    r=len(a)-1
    while(l<r):
        m=(l+r)//2
        if m==0 or a[m]>a[m-1] and (m==len(a)-1 or a[m]>a[m+1]):
            return a[m]
        elif a[m]>a[m-1]:
            l=m+1
        else:
            r=m-1
    return a[l]
print(findPeak(a))
            