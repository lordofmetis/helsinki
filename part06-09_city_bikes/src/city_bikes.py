# Write your solution here
def get_station_data(filename: str):
    dictionary = {}
    
    with open(filename) as file:
        for line in file:
            parts = line.split(";")
            if parts[0] == "Longitude":
                continue
            dictionary[parts[3]] = (float(parts[0]), float(parts[1]))

    return dictionary

def distance(stations: dict, station1: str, station2: str):
    import math
    
    if station1 in stations:
        longitude1 = stations[station1][0]
        latitude1 = stations[station1][1]
    if station2 in stations:
        longitude2 = stations[station2][0]
        latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict):
    import math

    results = []
    temp = []

    for m in stations:
        for n in stations:
            x_km = (stations[m][0] -stations[n][0]) * 55.26
            y_km = (stations[m][1] - stations[n][1]) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            results.append((m, n, distance_km))
            temp.append(distance_km)
    
    for station1, station2, distance in results:
        if distance == max(temp):
            return station1, station2, distance

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)