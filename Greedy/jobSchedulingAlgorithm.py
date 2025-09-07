# given 2 matrices of same size, job scheduling algorithm
a=[0,3,8,1,5,7,9]
b=[5,6,10,2,6,9,11]
def scheduleJobs(a,b):
    job=sorted(zip(a,b),key=lambda x:x[1])
    jobs=0
    end=-1
    for s,e in job:
        if end<s:
            jobs+=1
            end=e
    return jobs
print(scheduleJobs(a,b))