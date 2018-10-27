
import os
from os import rename, listdir
import cv2
import numpy as numpy

relevant_path = "."
included_extensions = ['jpg']
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]

fnames = listdir(relevant_path)
for i, fname in enumerate(file_names):
    try:
        rename(fname, "back_" + str(i + 1) + ".jpg")
        img = cv2.imread("back_" + str(i + 1) + '.jpg')
        resized_image = cv2.resize(img, (50, 50))
        cv2.imwrite("back_" + str(i + 1) + '.jpg', resized_image)
        print("image no :" + str(i + 1))

    except Exception as e:
        print(str(e))
