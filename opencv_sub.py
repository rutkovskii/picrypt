######################################################

# Image subtraction using OpenCV

######################################################


# importing opencv
import cv2
import numpy as np


def image_subtract(image1:np.ndarray, image2:np.ndarray):
    """Subtracts one image from another using cv2.subtract"""
    return cv2.subtract(image1, image2)


if __name__ == '__main__':
    # Example

    # reading the images
    image1 = cv2.imread("./assets/before.jpeg")
    image2 = cv2.imread("./assets/after.jpeg")

    # subtract the images
    result = image_subtract(image2, image1)

    # TO show the output
    cv2.imshow('Difference Image', subtracted)

    # To close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
