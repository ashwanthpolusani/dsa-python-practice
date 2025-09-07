# Given a 2d matrix of and a fire spot.
# The fire spreads to all surrounding trees in 4 directions.
# find the count of Unburned trees


def forestFire(forest,fire):
    n=len(forest)
    # Define a recursive function to burn trees
    def burn(f,i,j):
        # If the tree is already burnt or out of bounds, return
        if i<0 or j<0 or j==n or i==n or f[i][j]==0:
            return
        # Burn the tree
        f[i][j]=0
        # Recursively burn the adjacent trees
        burn(f,i-1,j)
        burn(f,i+1,j)
        burn(f,i,j-1)
        burn(f,i,j+1)

    # Call the burn function to burn all trees where fire started
    burn(forest,fire[0],fire[1])
    # Count the remaining trees
    remCount=0
    for row in forest:
        remCount+=row.count(1)
    # Return the remaining count of trees
    return f"Remaining Count of Trees: {remCount}"
   
# Define the forest
forest=[[1,0,0,1,1],
        [1,0,0,0,1],
        [1,0,0,1,0],
        [1,0,0,0,0],
        [1,0,0,0,1],]
# Define the fire location
fire=[0,4]
# Call the burn function to burn all trees where fire started
print(forestFire(forest,fire))