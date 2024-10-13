import math


def calculate_distance_meters(lat1: float, lon1: float, lat2: float, lon2: float):
    """
    Calculate the distance between two points on the Earth's surface specified by their latitude and longitude in meters.
    This function uses the Haversine formula to compute the great-circle distance between two points, which is the shortest distance over the Earth's surface.
    Parameters:
    lat1 (float): Latitude of the first point in decimal degrees.
    lon1 (float): Longitude of the first point in decimal degrees.
    lat2 (float): Latitude of the second point in decimal degrees.
    lon2 (float): Longitude of the second point in decimal degrees.
    Returns:
    float: Distance between the two points in meters.
    """

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
