"""
Detect button press when number of red pixels decreases in image,
detect shine when number of green and blue pixels increases in image.
"""

import os
import sys

import cv2
import numpy as np
import matplotlib.pyplot as plt


def bgr_array(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Invalid image path")
    width, height, colorvalue = img.shape
    return np.reshape(img, (width * height, colorvalue))


def bgr_values(image_path):
    array = bgr_array(image_path)
    return np.sum(array, axis=0)


def get_file_paths(directory_path):
    return [os.path.join(directory_path, file) for file in os.listdir(directory_path)]


if len(sys.argv) < 2:
    raise Exception("Must pass in a directory name")

files = get_file_paths(sys.argv[1])
rgb_trend = [[], [], []]

for file in files:
    print(file)
    try:
        blue, green, red = bgr_values(file)
        rgb_trend[0].append(red)
        rgb_trend[1].append(green)
        rgb_trend[2].append(blue)
    except ValueError:
        pass

print(rgb_trend)
x = np.arange(len(rgb_trend[0]))
plt.plot(x, rgb_trend[0], color="red")
plt.plot(x, rgb_trend[1], color="green")
plt.plot(x, rgb_trend[2], color="blue")
plt.show()
