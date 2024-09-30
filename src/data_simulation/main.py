from perlin_noise import PerlinNoise

print("Module loaded: data_simulation.main")

# Simulate cow natural temperature data variation with anomalies

noise = PerlinNoise(octaves=4, seed=1)

min_temp = 37.5
max_temp = 39.3
normal_anomaly_chance = 0.1  # Chance of a normal anomaly occurring

def generate_cow_temp_data():
    data = []
    for y in range(100):
        # Generate base temperature using Perlin noise
        temp = min_temp + (max_temp - min_temp) * noise([y / 10])
        
        # Round the temperature
        temp = round(temp, 2)

        data.append(temp)

    return data
        
        
