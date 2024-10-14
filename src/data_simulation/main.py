from perlin_noise import PerlinNoise
import random
from utils import map_range
from config import fever_trigger_pct, hypothermia_trigger_pct, min_temp, max_temp, max_heartrate, min_heartrate, tachycardia_trigger_pct, bradycardia_trigger_pct

print("Module loaded: data_simulation.main")

noise = PerlinNoise(octaves=4, seed=1)
noiseX = PerlinNoise(octaves=6)
noiseZ = PerlinNoise(octaves=12)


def next_temp(i):    
    if random.random() < fever_trigger_pct:  
        temp = max_temp + random.uniform(1, 2.2)
    elif random.random() >= fever_trigger_pct and random.random() < fever_trigger_pct + hypothermia_trigger_pct:
        temp = min_temp - random.uniform(0.5, 1.5)
    else:
        temp = min_temp + (max_temp - min_temp) * noise([i / 10])
    return round(temp, 2)

def next_heartrate(i):
    if random.random() < tachycardia_trigger_pct:
        heartrate = max_heartrate + random.uniform(5, 40)
    elif random.random() >= tachycardia_trigger_pct and random.random() < tachycardia_trigger_pct + bradycardia_trigger_pct:
        heartrate = min_heartrate - random.uniform(5, 20)
    else:
        heartrate = min_heartrate + (max_heartrate - min_heartrate) * noise([i / 10])
    bpm = round(heartrate)
    return round(bpm, 2)

def next_geo2d(i, interval):
    d = map_range(interval, 5, 10, 10_000_000, 1_000_000)

    lat = map_range(noiseX([i / d]), -1, 1, -90, 90)
    lon = map_range(noiseZ([i / d]), -1, 1, -180, 180)

    lat = round(lat, 4)
    lon = round(lon, 4)

    return lat, lon
