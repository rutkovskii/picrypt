# encrypt (shuffle)
# send
# receive
# decrypt (unshuffle)

import cv2
import numpy as np
import json
import requests
from numpy_json import encodeNumpyArray, decodeNumpyArray

def sender():
    # Send the samples to the server
    url = 'http://192.168.50.213:5000/runner'
    image1path = './assets/before.jpeg'
    image2path = './assets/after.jpeg'

    image1 = cv2.imread(image1path)
    image2 = cv2.imread(image2path)

    # Pack the samples into a list
    arrays_list = {'image1':encodeNumpyArray(image1), 'image2':encodeNumpyArray(image2)}

    r = send_samples(url,arrays_list)
    obj = json.loads(r.content)

    final_nparray = decodeNumpyArray(obj)
    final_nparray =  final_nparray.astype(np.uint8)
    cv2.imshow('Difference Image', final_nparray)

    # To close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()




def send_samples(url,arrays_list):
    # Pack the samples into a list
    entries_json = json.dumps(arrays_list)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, json=entries_json, headers=headers)
    #print(f"Status Code: {r.status_code}, Response: {r.json()}")
    return r

if __name__ == '__main__':
    sender()