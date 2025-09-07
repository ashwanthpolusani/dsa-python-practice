money=[5,5,5,10,20]
def change(money):
    five=0
    ten=0
    twenty=0
    for i in money:
        if i==5:
            five+=1
        elif i==10:
            ten+=1
            if five>0:
                five-=1
            else:
                return "Not Possible"
        else:
            twenty+=1
            if (ten>0 and five>0 ) or five>2:
                if ten>0:
                    ten-=1
                    five-=1
                else:
                    five-=3
            else:
                return "Not Possible"
    return "Possible"
print(change(money))