destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
attractions = [[] for i in destinations]


def destinationIndex(destination):
    return destinations.index(destination)

def travelerLocation(traveler):
    return destinationIndex(traveler[1])

def addAttraction(destination, attraction):
    try:
        attractions[destinationIndex(destination)].append(attraction)
    except:
        pass

def findCityAttractions(destination, interests):
    for i in attractions[destinationIndex(destination)]:
        for k in interests:
            if k in i[1]:
                return i[0]

def attractionsTraveler(traveler):
    tAttractions = findCityAttractions(traveler[1], traveler[2])
    msg = f"Hi {traveler[0]}, we think you'll like these places around {traveler[1]}: {tAttractions}."
    return msg


addAttraction("Paris, France", ["the Louvre", ["art", "museum"]])
addAttraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
addAttraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
addAttraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
addAttraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
addAttraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
addAttraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
addAttraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
addAttraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
addAttraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

smills_france = attractionsTraveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)