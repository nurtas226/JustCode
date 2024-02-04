# You have a collection with countries. There is information about the number of people and the area of the country. 
# We need to find the population density of each country and the most overpopulated country.

s = {
    "China": {'population': 1398700000,'area': 9596961},
    "India": {'population': 1256400000,'area': 3287263},
    "United States": {'population': 321000000,'area': 9833517},
    "Indonesia": {'population': 263000000,'area': 1904569},
    "Pakistan":{'population': 225000000,'area': 881913}
}

max_density_country = None
max_density = 0

for country, data in s.items():
    population = data['population']
    area = data['area']
    
    density = population / area
    
    print(f"{country}: population density {density}")
    
    if density > max_density:
        max_density = density
        max_density_country = country

print(f"\n The most populated country is {max_density_country}.")        



