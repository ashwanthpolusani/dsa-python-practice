# Give a matrix with 0's and 1's
# 1 represet land and 0 represent water
# a group of 1's at (top,left,bottom,right) 
# Note: Diagolal 1's are not be considered for formning group
# Write a program to count the total number of islands


def island(p):
    n=len(p)
    def findisland(a,i,j): #function to check the area of the island
        if i<0 or j<0 or i>=n or j>=n or a[i][j]==0 or a[i][j]==2:
            return 
        a[i][j]=2 # makes all 1's in that island to 2 to escape from infinite recursion.
        
        findisland(a,i-1,j)# Check the left cell   
        findisland(a,i+1,j)# Check the right cell
        findisland(a,i,j-1) # Check the top cell
        findisland(a,i,j+1)# Check the bottom cell
   
    c=0  # Initialize the count of islands
    # Loop through each element in the 2D list
    for i in range(n):
        for j in range(n):
            # If the element is 1, call the findisland function and increment the count
            if p[i][j]==1:
                findisland(p,i,j)
                c+=1
    # Return the count
    return c

# Define the 2D list
planet=[[1,0,0,1,1],
        [1,0,0,0,1],
        [1,0,0,1,0],
        [1,0,0,0,0],
        [1,0,0,0,1],]
# Call the island function and print the result
print(island(planet))