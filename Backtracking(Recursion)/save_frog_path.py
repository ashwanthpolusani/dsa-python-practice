# This code calculates how many different safe paths a frog can take from a start position 
# to reach the bottom-right corner of an n×n grid. The frog:
# Can only move right or down
# Must avoid danger zones
# Cannot go outside the grid boundaries
# Returns the count of all  possible valid paths

def frogPath(n,i,j,d):
    if i==n or j==n or (i,j) in d:
        return 0
    if i==n-1 and j==n-1:
        return 1
    return frogPath(n,i+1,j,d)+frogPath(n,i,j+1,d)

n=5
start=[0,1]
danger_zones=[(2,1),(4,1),(0,3),(4,3)]
res = frogPath(n, start[0] ,start[1],set(danger_zones))
print(res) 