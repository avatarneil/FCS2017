from GeoBases import GeoBase
geo_a = GeoBase(data='airports',verbose=False)

loc1 = (37.5665,126.9780)
loc2 = (59.9139,10.7522)

def price(loc1,loc2):
    airport1 = list(geo_a.findClosestFromPoint(loc1))
    airport2 = list(geo_a.findClosestFromPoint(loc2))
    distance = (geo_a.distance(airport1[0][1],airport2[0][1]) * .621371)
    if (geo_a.get(airport1[0][1],'country_code') == geo_a.get(airport2[0][1],'country_code')):
        price = (.032 * (distance*2)) + 230
    else:
        price = (.08 * (distance*2)) + 200
    return price
print(price(loc1,loc2))

