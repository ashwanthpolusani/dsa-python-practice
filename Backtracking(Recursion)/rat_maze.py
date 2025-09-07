# Given a rat maze(a 2D array)
# The rat starts at (0,0) and ends at (n-1,n-1)
# Check how many paths available for the rat to move from start to end


# Define a function to solve the maze
def maze(a,n,i=0,j=0):
    # If the current position is out of bounds or a wall, return 0
    if i>=n or j>=n or a[i][j]==0:
        return 0
    # If the current position is the end of the maze, return 1
    if i==n-1 and j==n-1:
        return 1
    # Recursively call the function to move right and down
    return maze(a,n,i,j+1) + maze(a,n,i+1,j)
# Define the maze
a=[[1,0,0,0,0],
   [1,1,1,0,0],
   [1,0,1,0,0],
   [1,0,1,1,1],
   [1,1,1,1,1]]

# Get the size of the maze
n=len(a)
# Print the number of paths to the end of the maze
print(maze(a,n))
