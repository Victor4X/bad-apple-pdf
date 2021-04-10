# ~Stolen from~ Inspired by: https://github.com/kevinjycui/bad-apple

from PIL import Image

import time
import os
import json

WIDTH = 96
HEIGHT = 72

matrix_arr = []

for i in range(1, 6573):
    print(i)
    with Image.open("data/frames/" + str(i) + ".bmp") as im:
        px = im.load()
    matrix = []
    for x in range(HEIGHT):
        row = []
        for y in range(WIDTH):
            if px[y,x][0] < 125:
                row.append(1)
            else:
                row.append(0)
            
            # if px[y,x][0] < 85:
            #     row.append(1)
            # elif px[y,x][0] > 170:
            #     row.append(0)
            # else:
            #     row.append(2)


        matrix.append(row)
    matrix_arr.append(matrix)
        


with open('data2.json', 'w+') as f:
    json.dump(matrix_arr, f)