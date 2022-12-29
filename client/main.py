import numpy as np
import json, requests
import logging
from numpy_json import encodeNumpyArray, decodeNumpyArray
import crypto as cr


log = logging
log.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def sender(url,image1path='./client/assets/before.jpeg',image2path='./client/assets/after.jpeg', show_images=False):
    """Must run from root folder"""
    log.info("")
    # Create Encryption Instance
    log.info("Creating Encryption Instance")
    s = cr.generate_S(cr.__generate_key())

    # Read Images using OpenCV
    log.info("Reading Original Images")
    image1, image2 = cr.cv2_open_images(image1path, image2path)

    # Show Images
    if show_images:
        log.info("Showing Original Images")
        cr.cv2_show_images(image1, "Before Move", image2, "After Move")

    # Encrypt Images
    log.info("Encrypting Original Images")
    enc_buffer1, enc_buffer2 = cr.encrypt_images(s, image1, image2)

    # Show Encrypted Images
    if show_images:
        log.info("Showing Encrypted Images")
        cr.cv2_show_images(enc_buffer1, "Before Move Encrypted", enc_buffer2, "After Move Encrypted")

    # Pack the samples into a list
    log.info("Packing Encrypted Images")
    arrays_list = {'image1':encodeNumpyArray(enc_buffer1), 'image2':encodeNumpyArray(enc_buffer2)}

    # Send the samples to the server
    log.info("Sending Encrypted Images to API")
    response = send_samples(url,arrays_list)

    obj = json.loads(response.content)

    log.info("Decoding Encrypted Image")
    final_nparray = decodeNumpyArray(obj)
    final_nparray =  final_nparray.astype(np.uint8)

    # Show Subtracted Encrypted Image
    if show_images:
        log.info("Showing Subtracted Encrypted Image")
        cr.cv2_show_images(final_nparray, "Subtracted Encrypted Image")

    # Decrypt Subtracted Encrypted Image
    log.info("Decrypting Subtracted Image")
    dec_buffer_final = cr.decrypt_image(s,final_nparray)

    # Show Decrypted Subtracted Image
    if show_images:
        log.info("Showing Decrypted Subtracted Image")
        cr.cv2_show_images(dec_buffer_final, "Decrypted Subtracted Image")

    # To close the window
    if show_images:
        log.info("Check Windows to see the Images, Press any key to close the windows")
        cr.cv2_window_sleeper()

    log.info("")


def send_samples(url,arrays_list):
    # Pack the samples into a list
    entries_json = json.dumps(arrays_list)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.post(url, json=entries_json, headers=headers)
    log.info(f"Status Code: {response.status_code}")
    return response

if __name__ == '__main__':

    # Inputs
    url = 'http://10.160.10.113:7000'               # Insert your link
    image1path = './client/assets/before.jpeg'      # Place your images in the client/assets folder
    image2path = './client/assets/after.jpeg'       # And change the path here


    full_url = f"{url}/api/runner"

    # Turn On the client
    sender(full_url, image1path, image2path, show_images=True)