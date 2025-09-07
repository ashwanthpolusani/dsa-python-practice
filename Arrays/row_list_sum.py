# Given  a list and a 2D matrix
# For each row make the sum of (row element*list element ) at that Index


#Define a function to find the row sum of a matrix
def findrowsum(l,mat):
    #Create an empty list to store the row sums
    res=[]
    #Loop through each row in the matrix
    for row in mat:
        #Initialize a variable to store the sum of the row
        s=0
        #Loop through each element in the row
        for i in range(len(row)):
            #Add the product of the element in the row and the corresponding element in the list to the sum
            s+=row[i]*l[i]
        #Append the sum to the list of row sums
        res.append(s)
    #Return the list of row sums
    return res
#Define a list of weights
l=[8,7,6,5,2]
#Define a matrix
mat=[[0,1,1,0,1],
     [1,1,0,0,1],
     [0,0,0,1,1],
     [0,1,0,0,0]]
#Print the row sums of the matrix
print(findrowsum(l,mat))