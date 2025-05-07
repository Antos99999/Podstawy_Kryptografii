import colorsys
from PIL import Image
import hashlib
import struct

class KeyedPRNG:
    def __init__(self, key):
        self.key = key.encode('utf-8') if isinstance(key, str) else key
        self.counter = 0

    def _get_hash(self):
        data = self.key + struct.pack(">Q", self.counter)
        hash_bytes = hashlib.sha256(data).digest()
        self.counter += 1
        return int.from_bytes(hash_bytes, 'big')

    def randint(self, a, b):
        return a + self._get_hash() % (b - a + 1)


def encoding(d,n,region_size,key):
    img = Image.open("../resources/image1.jpg").convert('RGB')
    px = img.load()
    prng = KeyedPRNG(key)
    picked_area = []
    brightnesses = []
    brightnes = 0

    for i in range(n+1):
        x = prng.randint(0, img.size[0] - region_size)
        y = prng.randint(0, img.size[1] - region_size)
        picked_area.append((x, y))

    for i in range(n):
        brightness = average_brightness(px, picked_area[i][0], picked_area[i][1], region_size)
        brightnesses.append(brightness)

    for i in range(n):
        if i+1 < len(brightnesses):
            brightnes += (brightnesses[i] - brightnesses[i+1])
    print(f"Jasność: {float(int(brightnes))}")

    #print(picked_area)
    original_brightness = []

    for index, (x_start, y_start) in enumerate(picked_area):
        count = 0

        for dx in range(region_size):
            for dy in range(region_size):
                x = x_start + dx
                y = y_start + dy
                r, g, b = px[x, y]

                if index % 2 == 0:
                    # rozjaśnianie
                    r = min(r + d, 255)
                    g = min(g + d, 255)
                    b = min(b + d, 255)
                else:
                    # przyciemnianie
                    r = max(r - d, 0)
                    g = max(g - d, 0)
                    b = max(b - d, 0)

                brightness_after = (r + g + b) / 3

                px[x, y] = (r, g, b)
                count += 1

                original_brightness.append(brightness_after / count)

    img.save("../resources/image_wodny.jpg")
    #img.show()
    img = Image.open("../resources/image_wodny.jpg").convert('RGB')
    px = img.load()

    # Sprawdzanie S'n zgodnie ze wzorem:
    sum1 = 0
    sum2 = 2 * d * n
    tmp = 0

    for i in range(n):
        brightness = average_brightness(px, picked_area[i][0], picked_area[i][1], region_size)
        brightnesses.append(brightness)

    for i in range(0,n):
        if i+1 < len(brightnesses):
            sum1 += ((brightnesses[i]+d) - (brightnesses[i+1]-d))
            tmp += (brightnesses[i] - brightnesses[i+1])
    sum2 = sum2 + tmp

    #print(f"Jasość po nałożeniu znaku wodnego = {sum2}")

def average_brightness(px, x_start, y_start, region_size):
    total_brightness = 0
    count = 0

    for dx in range(region_size):
        for dy in range(region_size):
            x = x_start + dx
            y = y_start + dy
            r, g, b = px[x, y]
            brightness = (r + g + b) / 3
            total_brightness += brightness
            count += 1

    return total_brightness / count if count > 0 else 0

def decoding(d,n,region_size,key):
    img = Image.open("../resources/image_wodny.jpg").convert('RGB')
    px = img.load()
    prng = KeyedPRNG(key)
    picked_area = []

    for i in range(n):
        x = prng.randint(0, img.size[0] - region_size)
        y = prng.randint(0, img.size[1] - region_size)
        picked_area.append((x, y))

    brightnesses = []
    detection2 = 0
    #print(picked_area)
    for i in range(n):
        brightness = average_brightness(px, picked_area[i][0], picked_area[i][1], region_size)
        brightnesses.append(brightness)

    for i in range(n):
        if i+1 < len(brightnesses):
            detection2 += (brightnesses[i] - brightnesses[i+1])
    print(f"Jasność przy sprawdzaniu znaku wodnego = {detection2}")

if __name__ == '__main__':
    key = "Tajny Klucz"
    d = 50
    n = 17
    region_size = 10
    encoding(d,n,region_size,key)
    decoding(d,n,region_size,key="test")
