from perlin_noise import PerlinNoise

print("Module loaded: data_simulation.main")

# Simulate animal natural temperature data variation with anomalies

noise = PerlinNoise(octaves=4, seed=1)

min_temp = 37.5
max_temp = 39.3

def next_temp(i):
    temp = min_temp + (max_temp - min_temp) * noise([i / 10])
    return round(temp, 2)
