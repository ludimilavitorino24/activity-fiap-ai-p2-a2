from perlin_noise import PerlinNoise
import random

print("Module loaded: data_simulation.main")

noise = PerlinNoise(octaves=4, seed=1)
noiseX = PerlinNoise(octaves=6)
noiseZ = PerlinNoise(octaves=12)

FEVER_TRIGGER_PCT = 0.083
MIN_TEMP = 37.5
MAX_TEMP = 39.3
TACHYCARDIA_TRIGGER_PCT = 0.022
MIN_HEARTRATE = 60
MAX_HEARTRATE = 80

def next_temp(i):    
    if random.random() < FEVER_TRIGGER_PCT:  
        temp = MAX_TEMP + random.uniform(1, 2.2)  
    else:
        temp = MIN_TEMP + (MAX_TEMP - MIN_TEMP) * noise([i / 10])
    return round(temp, 2)

def next_heartrate(i):
    if random.random() < TACHYCARDIA_TRIGGER_PCT:
        heartrate = MAX_HEARTRATE + random.uniform(5, 40)
    else:
        heartrate = MIN_HEARTRATE + (MAX_HEARTRATE - MIN_HEARTRATE) * noise([i / 10])
    bpm = round(heartrate)
    return round(bpm, 2)

def map_range(value, start1, stop1, start2, stop2):
    return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))

def next_geo2d(i, interval):
    d = map_range(interval, 5, 10, 10_000_000, 1_000_000)

    lat = map_range(noiseX([i / d]), -1, 1, -90, 90)
    lon = map_range(noiseZ([i / d]), -1, 1, -180, 180)

    lat = round(lat, 4)
    lon = round(lon, 4)

    return lat, lon

