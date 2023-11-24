import cv2
import numpy as np
from PIL import Image
import pickle

image = cv2.imread("./screenshot3.png")

image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

np.save('size1.txt', image)

# image = [
#     [[19, 19, 12], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24]],
#     [[19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24]],
#     [[19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [19, 19, 19], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24], [24, 24, 24]],
# ]

# print(len(image))

height = len(image)

width = len(image[1])

print(str(width) + "*" + str(height))

previousRgb = [-1, -1, -1]

compressedImageData = []

def saveColorWithRepetition(repetition, column):
    # print(str(previousRgb) + " repeated: " + str(repetition))
    if len(compressedImageData) <= column:
        # erstelle Zeile
        compressedImageData.append([])
    data = [ previousRgb[0], previousRgb[1], previousRgb[2] ]
    if repetition != 1:
        data.append(repetition)
    compressedImageData[column].append(data)
    # print(previousRgb.append(repetition))
    # np.append(compressedImageData[column], [np.append(previousRgb, repetition)])


for i in range(height): 
    column = image[i]
    # print("column: "+ str(i))
    # print(column)
    counter = 0
    for j in range(width):       
        if j != 0:
            counter += 1
            if (column[j][0] != previousRgb[0] or column[j][1] != previousRgb[1] or column[j][2] != previousRgb[2]) or j == width - 1:
                # bedeutet es ist nicht gleich, speicher die vorherige farbe mit der anzahl an wiederholungen, aber fürs erste nur ausgeben
                if j == width - 1:
                    saveColorWithRepetition(counter + 1, i)
                else:
                    saveColorWithRepetition(counter, i)
                counter = 0
        previousRgb = column[j]
        
f2 = open("size2.txt", "w")
f2.write(str(compressedImageData))
f2.close()