import math

def get_area(r):
    return math.pi * math.pow(r,2)

print(f"Result: {get_area(3)}")

def get_volume(r):
    return 4/3 * math.pi * math.pow(r,3)

print(f"Result2: {get_volume(3)}")

deg = 180
rad = math.radians(deg)
print(f"Result3: {rad}")