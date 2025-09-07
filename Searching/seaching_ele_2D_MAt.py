# Seartching a element in 2D matrix
def search2D(a,ele):
    l=True
    for i in range(len(a)):
        flag=False
        for j in range(len(a[i])):
            if a[i][j]==ele:
                print("Found")
                flag=True
                l=False
                break
        if flag:
            break
    if l:
        print("Not found")
    return i,j

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(search2D(a,10))