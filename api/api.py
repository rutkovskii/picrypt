from numpy_json import encodeNumpyArray, decodeNumpyArray
from flask import Blueprint, request, jsonify
import json
import cv2
import numpy as np


api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/')
def index():
    return 'Hello, World!'


def decodeJsons(arr1,arr2):
    return decodeNumpyArray(arr1), decodeNumpyArray(arr2)

def encodeJson(arr):
    return encodeNumpyArray(arr)


def image_subtract(image1:np.ndarray, image2:np.ndarray):
    """Subtracts one image from another using cv2.subtract"""
    return cv2.subtract(image1, image2)


@api_blueprint.route('/runner', methods=['POST'])
def runner():
    # image1, image2 = decodeJsons(request.json['image1'], request.json['image2'])
    obj = json.loads(request.json)
    image1, image2 = decodeJsons(obj['image1'], obj['image2'])
    final_image = image_subtract(image1, image2)
    final_encoded_image = encodeJson(final_image)
    #print(json.dumps(final_encoded_image))
    return json.dumps(final_encoded_image)