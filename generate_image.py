import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

from noise import *

# If you're gonna run this change the amplitude to 256 in noise.py
# (Hi Colten)
OUTPUT_SIZE = (100, 100)

# noise = Noise1D()
# x = np.linspace(0, 6, 1000)
# y = np.array([])
# for x1 in x:
#     y = np.append(y, noise.noise(x1))
# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot(x, y)  # Plot some data on the axes.
# plt.show()

noise = Noise2D()

image = Image.new("RGB", OUTPUT_SIZE)
pixels = image.load()
for x in range(OUTPUT_SIZE[0]):
    for y in range(OUTPUT_SIZE[1]):
        pixels[x,y] = (int(noise.noise(x, y)),) * 3

image.save("output.png")