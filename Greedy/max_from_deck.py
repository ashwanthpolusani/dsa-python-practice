# give a array of deck of cards and integer k.
# remove k cards from the deck from the top or bottom such that the sum becomes max

def makeCards(deck,k):
    l=0
    r=len(deck)
    lsum=0
    while l<k:
        lsum+=deck[l]
        l+=1
    rsum=0
    m=lsum+rsum
    while l>0:
        l-=1
        r-=1
        rsum+=deck[r]
        lsum-=deck[l]
        m=max(m,lsum+rsum)
        print(lsum,rsum)
    print(m)

def makeCards1(deck,k):
    n=len(deck)
    tsum=0
    for i in range(k):
        tsum+=deck[i]
    m=tsum
    for i in range(k-1,-1,-1):
        tsum=tsum+deck[n+i-k]-deck[i]
        m=max(m,tsum)
        print(tsum,deck[n+i-k],deck[i])
    print(m)


deck=[400,2,7,20,8,60,1000,1]
k=3
print(makeCards(deck,k))
print(makeCards1(deck,k))