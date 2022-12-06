######################################################

# Image subtraction using Pillow

######################################################


# Python example program for image subtraction

from PIL import Image
import numpy as np
import io

# Paths of two image frames

image1Path = "./assets/before.jpeg"

image2Path = "./assets/after.jpeg"

# Open the images
# with open(image1Path, "rb") as image1File:
#     bytes_read = image1File.read()
#     print(dir(io.BytesIO(bytes_read)))
#     print(io.BytesIO(bytes_read).getvalue())

# Open the images
image1 = Image.open(image1Path)
# print(image1)

image2 = Image.open(image2Path)

# Get the image buffer as ndarray

buffer1 = np.asarray(image1)

buffer2 = np.asarray(image2)

# Subtract image2 from image1

buffer3 = buffer1 - buffer2

# Construct a new Image from the resultant buffer

differenceImage = Image.fromarray(buffer3)

# Display all the images including the difference image

#image1.show()

#image2.show()

#differenceImage.show()
