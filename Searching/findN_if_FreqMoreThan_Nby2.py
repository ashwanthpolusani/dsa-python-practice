# find the element with frequency more than n/2
# Note: The input definitely has a majority element which  deinitely occurs more than n/2 times
a=[1,1,2,2,3,1,1,3,7]
count=0
for i in a:
    if count==0:
        ele=i
        count=1
    elif i==ele:
        count+=1
    else:
        count-=1
print(ele)