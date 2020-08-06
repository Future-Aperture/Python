premiumShip = 125

def groundShip(weight):
    if weight <= 2:
        return weight * 1.5 + 20
    elif 2 < weight <= 6:
        return weight * 3 + 20
    elif 6 < weight <= 10:
        return weight * 4 + 20
    else:
        return weight * 4.5 + 20

def droneShip(weight):
    if weight <= 2:
        return weight * 4.5
    elif 2 < weight <= 6:
        return weight * 9
    elif 6 < weight <= 10:
        return weight * 12
    else:
        return weight * 14.25

def bestShip(w):
    lst = [groundShip(w), droneShip(w), premiumShip]
    lstName = ["Ground Shipping", "Drone Shipping", "Premium Shipping"]

    print(f"The cheapest shipping for you is: {lstName[lst.index(min(lst))]}\nIt will cost you: US$ {round(min(lst), 2):.2f}\n")
    

bestShip(4.8)
bestShip(41.5)