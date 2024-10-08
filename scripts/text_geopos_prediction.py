import math

def calculate_distance_meters(lat1: float, lon1: float, lat2: float, lon2: float):
    R = 6371000.0  # Radius of the Earth in meters

    # Convert degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Differences in coordinates
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Haversine formula
    a = (math.sin(dlat / 2) ** 2) + (
        math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in meters
    distance = R * c

    return distance

data = []

for i in range(10):
    data.append(next_geo2d(i, 5))
    
    if(i > 0):
        dist = calculate_distance_meters(data[i-1][0], data[i-1][1], data[i][0], data[i][1])
        print(dist)
    