from numpy_json import encodeNumpyArray, decodeNumpyArray
from flask import Blueprint, request
import json, cv2
import numpy as np
import logging


api_blueprint = Blueprint('api', __name__)


log = logging
log.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)



@api_blueprint.route('/')
def index():
    return 'Hello, ECE597 NP!'


def decodeJsons(arr1,arr2):
    return decodeNumpyArray(arr1), decodeNumpyArray(arr2)


def encodeJson(arr):
    return encodeNumpyArray(arr)


def image_subtract(image1:np.ndarray, image2:np.ndarray):
    """Subtracts one image from another using cv2.subtract"""
    return cv2.subtract(image1, image2)


@api_blueprint.route('/api/runner', methods=['POST'])
def runner():
    log.info("")
    log.info("Object is received")
    obj = json.loads(request.json)
    log.info("Decoding Encrypted Images")
    image1, image2 = decodeJsons(obj['image1'], obj['image2'])
    log.info("Subtracting Encrypted Images")
    final_image = image_subtract(image1, image2)
    log.info("Encoding Subtracted Image")
    final_encoded_image = encodeJson(final_image)
    log.info("Returning Subtracted Image")
    log.info("")
    return json.dumps(final_encoded_image)