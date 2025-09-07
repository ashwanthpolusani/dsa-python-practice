# given a array and a key. check if the key exists in that array.
# if key is not found return -1 else return highghest index of the accurrence of that array

def search(a,k):
    for i in range(len(a)-1,-1,-1):
        if a[i]==k:
            return i
    return -1

a=[2,4,3,1,4,2,3,4,5]
k=49
print(search(a,k))