### MAP ###

import math

def area(r):
    return math.pi * (r**2)

radii = [2, 5, 7, 1]


# 1. for loop
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)


# 2. map
m = list(map(area, radii))

print(m)



### FILTER ###
import statistics

data = [1.3, 2.8, 4.2, 5.7, 3.3]

avg = statistics.mean(data)
print(avg)

f = list(filter(lambda x: x > avg, data))
print(f)

# Second example: Remove missing data
countries = ["", "Brasil", "", "Denmark"]

f = list(filter(None, countries))
print(f)
