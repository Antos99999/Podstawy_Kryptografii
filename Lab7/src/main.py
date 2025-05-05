from PIL import Image
import numpy as np
import random

from matplotlib import pyplot as plt


def main():
    sekret = "Ala ma kota"
    print(f"Sekret: {sekret}")
    bin_sekret = ''.join(format(ord(i), '08b') for i in sekret)
    print(f"Sekret binarnie: {bin_sekret}")
    sekret_len = len(bin_sekret)
    #print(sekret_len)
    obraz = Image.open("../resources/obraz.jpg")
    obraz_np = np.array(obraz).astype(np.uint8)
    if bin_sekret[-1] == "0":
        bin_sekret = bin_sekret.ljust(obraz_np.size,"1")
    else:
        bin_sekret = bin_sekret.ljust(obraz_np.size,"0")

    final_obraz = []
    sekret_index = 0


    for row in obraz_np:
        tmp_row = []
        for pixel in row:
            r = bin(pixel[0])[2:].zfill(8)
            g = bin(pixel[1])[2:].zfill(8)
            b = bin(pixel[2])[2:].zfill(8)

            if sekret_index < len(bin_sekret):
                r = r[:-1] + bin_sekret[sekret_index]
                sekret_index += 1
            if sekret_index < len(bin_sekret):
                g = g[:-1] + bin_sekret[sekret_index]
                sekret_index += 1
            if sekret_index < len(bin_sekret):
                b = b[:-1] + bin_sekret[sekret_index]
                sekret_index += 1

            new_pixel = [int(r, 2), int(g, 2), int(b, 2)]
            tmp_row.append(new_pixel)
        final_obraz.append(tmp_row)

                #print(r[-1])
                #print(sekret_char)
                #print(pixel)
                #print(bin(pixel[0]),bin(pixel[1]),bin(pixel[2]))
                #print(bin(obraz_np[pixel]))
    final_array = np.array(final_obraz, dtype=np.uint8)
    output_image = Image.fromarray(final_array)
    output_image.save("../output/zmodyfikowany_obraz.png")

    odtworzony_sekret = ""

    for row in final_array:
        for pixel in row:
            r = bin(pixel[0])[2:].zfill(8)
            g = bin(pixel[1])[2:].zfill(8)
            b = bin(pixel[2])[2:].zfill(8)
            odtworzony_sekret = odtworzony_sekret + r[-1] + g[-1] + b[-1]

    counter = 0
    letters = 0
    letter_type = ""
    for char in range(len(odtworzony_sekret)):
        if odtworzony_sekret[char] == odtworzony_sekret[char+1]:
            counter += 1
            letters += 1
        else:
            counter = 0
            letters += 1

        if counter > 9:
            odtworzony_sekret = odtworzony_sekret[:letters]
            letter_type = odtworzony_sekret[letters-1]
            break

    i = len(odtworzony_sekret) - 1
    while i >= 0 and odtworzony_sekret[i] == letter_type:
        i -= 1

    odtworzony_sekret = odtworzony_sekret[:i+1]

    print(f"Odtworzony sekret binarnie: {odtworzony_sekret}")

    odtworzony_sekret = ''.join(chr(int(odtworzony_sekret[i:i+8], 2)) for i in range(0, len(odtworzony_sekret), 8))

    print(f"Odtworzony sekret: {odtworzony_sekret}")

if __name__ == "__main__":
    main()