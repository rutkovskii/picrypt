######################################################

# Attempted to start working on pixel by pixel subtraction
# But realised it would be unfeasible because even after 10 minutes with input x1 = 255, and x2 = 256
# the compiler has not compiled

# Also tried to use cv2.subtract, but seems that library does not support homomorphic encryption on np.ndarrays

# https://github.com/zama-ai/concrete-numpy

######################################################

import concrete.numpy as cnp
import numpy as np
import cv2
from opencv_sub import image_subtract

def rgb_subtract(x1, x2):
    return x1 - x2


image1_path = "./assets/before.jpeg"
image2_path = "./assets/after.jpeg"

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)
print(type(image1))

scale_percent = 30 # percent of original size
width = int(image1.shape[1] * scale_percent / 100)
height = int(image1.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized1 = cv2.resize(image1, dim, interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(image2, dim, interpolation=cv2.INTER_AREA)


#compiler = cnp.Compiler(rgb_subtract, {"x1":'clear', "x2":'encrypted'})
#inputset = [(255, 244)]


# print(f"Compiling...")
# circuit = compiler.compile(inputset)
# examples = [(255, 244),(233, 244)]
# for example in examples:
#     decrypted = circuit.encrypt_run_decrypt(*example)
#     encrypted = circuit.encrypt(*example)
# #     imshow("Difference Image Normal", decrypted)
# #     imshow("Difference Image Encrypted", encrypted)
# #
# #     waitKey(0)
# #     destroyAllWindows()
#
#     print(f"Evaluation of {' + '.join(map(str, example))} homomorphically = {decrypted}, encrypted = {encrypted}")