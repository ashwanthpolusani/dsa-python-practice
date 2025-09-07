jobs=[4,3,7,1,6,2]
def waitingTime(jobs):
    jobs.sort()
    s=0
    current=0
    for i in range(1,len(jobs)):
        current=current+jobs[i-1]
        s+=current
    print(s)
    return s//(len(jobs))
print(waitingTime(jobs))
