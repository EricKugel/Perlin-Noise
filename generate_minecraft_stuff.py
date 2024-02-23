"""
Look up how to use function command in minecraft... it's hard to explain
"""

from noise import *

# If you're gonna run this you gotta tweak the amplitude and frequency and stuff in noise.py
# (Hi Colten)
OUTPUT_SIZE = (100, 100)
# START_COORD = (0, -60, 0)
START_COORD = (-328, -60, -136)

x, y, z = START_COORD

commands = [f"fill {' '.join(map(str, START_COORD))} {x + OUTPUT_SIZE[0]} {y + 10} {z + OUTPUT_SIZE[1]} air"]

noise = Noise2D()
for dx in range(OUTPUT_SIZE[0]):
    for dz in range(OUTPUT_SIZE[1]):
        dy = int(noise.noise(dx, dz))
        commands.append(f"fill {x + dx} {y} {z + dz} {x + dx} {y + dy} {z + dz} minecraft:grass_block destroy")

with open("output.mcfunction", "w") as file:
    file.write("\n".join(commands))