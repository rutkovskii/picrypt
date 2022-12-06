import cv2
import numpy as np
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


def convert_to_ndarray(image1,image2):
    buffer1 = np.asarray(image1)
    buffer2 = np.asarray(image2)

    return buffer1,buffer2


def __generate_key():
    return randint(10001, 99999)


def generate_S(key=1234):
    s = imageshuffle.Rand(key)
    return s


def encrypt_images(s,buffer1=None,buffer2=None):
    return s.enc(buffer1),s.enc(buffer2)


def decrypt_image(s,buffer):
    return s.dec(buffer)



# try cv2 image

def crypto_runner(path1="./assets/before.jpeg",path2="./assets/after.jpeg"):
    s = generate_S(__generate_key())

    # cv2
    image1,image2 = cv2_open_images(path1,path2)
    # print(image1)
    cv2_show_images(image1,"Before Move",image2,"After Move")
    enc_buffer1, enc_buffer2 = encrypt_images(s, image1, image2)
    cv2_show_images(enc_buffer1,"Before Move Encrypted", enc_buffer2, "After Move Encrypted")


    dec_buffer1 = decrypt_image(s,enc_buffer1)
    cv2_show_images(dec_buffer1,"Decrypted Image 1")


if __name__ == '__main__':
    crypto_runner()




