from perlin_noise import PerlinNoise

print("Module loaded: data_simulation.main")

noise = PerlinNoise(octaves=4, seed=1)
noiseX = PerlinNoise(octaves=6)
noiseZ = PerlinNoise(octaves=12)

MIN_TEMP = 37.5
MAX_TEMP = 39.3
MIN_HEARTRATE = 60
MAX_HEARTRATE = 80

def next_temp(i):
    temp = MIN_TEMP + (MAX_TEMP - MIN_TEMP) * noise([i / 10])
    return round(temp, 2)

def next_heartrate(i):
    heartrate = MIN_HEARTRATE + (MAX_HEARTRATE - MIN_HEARTRATE) * noise([i / 10])
    bpm = round(heartrate)
    return bpm

def map_range(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

def next_geo2d(i, interval):
    d = map_range(interval, 5, 10, 10_000_000, 1_000_000)

    lat = map_range(noiseX([i / d]), -1, 1, -90, 90)
    lon = map_range(noiseZ([i / d]), -1, 1, -180, 180)

    lat = round(lat, 4)
    lon = round(lon, 4)

    return lat, lon
