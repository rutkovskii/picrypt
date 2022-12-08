import cv2
from imageshuffle import imageshuffle
from random import randint


def cv2_open_images(path1,path2):
    return cv2.imread(path1),cv2.imread(path2)


def cv2_show_images(image1,image1_text,image2=None,image2_text=None):
    cv2.imshow(image1_text,image1)
    if image2 is not None:
        cv2.imshow(image2_text,image2)


def cv2_window_sleeper():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def __generate_key():
    """Create a random key for the encryption"""
    return randint(10001, 99999)


def generate_S(key=1234):
    """Create an instance of the imageshuffle class for encryption and decrytion"""
    return imageshuffle.Rand(key)


def encrypt_images(s, buffer1=None, buffer2=None):
    """Encrypt the images using the imageshuffle class"""
    return s.enc(buffer1), s.enc(buffer2)


def decrypt_image(s,buffer):
    """Decrypt the images using the imageshuffle class"""
    return s.dec(buffer)





