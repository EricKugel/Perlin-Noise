import numpy as np

FREQUENCY = .05
SIZE = int(100 * FREQUENCY)
AMPLITUDE = 12

def lerp(val1, val2, t):
    return (val2 - val1) * t + val1

def smooth_step(t):
    return t * t * (3 - 2 * t)

class Noise():
    def __init__(self, n):
        self.n = n
        self.lattice = np.random.rand(*([SIZE]*n))
        print(self.lattice)
    def consider(coords):
        pass

class Noise1D():
    def __init__(self):
        self.n = 1
        self.lattice = np.random.rand(SIZE)
        # self.lattice = np.linspace(0, SIZE, SIZE + 1)
        self.lattice *= AMPLITUDE
    def noise(self, x):
        x *= FREQUENCY
        x1 = int(x) % SIZE
        x2 = (x1 + 1) % SIZE
        t = x % 1
        return lerp(self.lattice[x1], self.lattice[x2], smooth_step(t))
    
class Noise2D():
    def __init__(self):
        self.n = 2
        self.lattice = np.random.rand(SIZE, SIZE)
        self.lattice *= AMPLITUDE
    # Interpolate x along y top, along y bottom... interpolate y
    def noise(self, x, y):
        x *= FREQUENCY
        y *= FREQUENCY
        x1 = int(x) % SIZE
        x2 = (x1 + 1) % SIZE
        y1 = int(y) % SIZE
        y2 = (y1 + 1) % SIZE
        tx = x % 1
        ty = y % 1
        val1 = lerp(self.lattice[x1][y1], self.lattice[x2][y1], smooth_step(tx))
        val2 = lerp(self.lattice[x1][y2], self.lattice[x2][y2], smooth_step(tx))
        return lerp(val1, val2, smooth_step(ty))
