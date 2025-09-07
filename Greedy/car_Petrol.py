def travel(petrol):
    car=0
    for bunk in petrol:
        if bunk>car:
            car=bunk
        if car == 0:
            return "Not Possible"
        car-=1
    return "Possible"

petrol=[2,3,1,0,1,3,0]
print(travel(petrol))