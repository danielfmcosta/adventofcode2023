file = open("C:/Users/costa/OneDrive/Documentos/Programming/Extras/adventofcode2023/day05/input.txt", "r")
content = file.read()

mapped_content = [x for x in content.split(':') if x != '']
seeds = [x for x in mapped_content[1][:-18].split() if x != '']
to_soil_map = [x for x in mapped_content[2][:-24].split('\n') if x != '']
to_fertilizer_map = [x for x in mapped_content[3][:-25].split('\n') if x != '']
to_water_map = [x for x in mapped_content[4][:-20].split('\n') if x != '']
to_light_map = [x for x in mapped_content[5][:-26].split('\n') if x != '']
to_temperature_map = [x for x in mapped_content[6][:-29].split('\n') if x != '']
to_humidity_map = [x for x in mapped_content[7][:-26].split('\n') if x != '']
to_location_map = [x for x in mapped_content[8].split('\n') if x != '']

def seed_to_next(seed, to_next):
    next_seed = seed
    for i in range(len(to_next)):
        line= to_next[i].split()
        if(seed >= int(line[1]) and seed <= int(line[1])+int(line[2])):
            next_seed = seed - int(line[1]) + int(line[0])
    return next_seed

min_location = float('inf')

for i in range(len(seeds)):
    soil = seed_to_next(int(seeds[i]), to_soil_map)
    fertilizer = seed_to_next(soil, to_fertilizer_map)
    water = seed_to_next(fertilizer, to_water_map)
    light = seed_to_next(water, to_light_map)
    temperature = seed_to_next(light, to_temperature_map)
    humidity = seed_to_next(temperature, to_humidity_map)
    location = seed_to_next(humidity, to_location_map)
    if(location<min_location):
        min_location = location

print(min_location)
file.close()