from PIL import Image

import noise

noise_r = noise.Noise2D()
noise_g = noise.Noise2D()
noise_b = noise.Noise2D()

OUTPUT_SIZE = (700, 700)

image = Image.new("RGB", OUTPUT_SIZE)
pixels = image.load()
for x in range(OUTPUT_SIZE[0]):
    for y in range(OUTPUT_SIZE[1]):
        pixels[x,y] = (int(noise_r.noise(x, y)), int(noise_g.noise(x, y)), int(noise_b.noise(x, y)))

image.save("colorful.png")