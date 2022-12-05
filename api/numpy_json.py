import json
from json import JSONEncoder
import numpy

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def encodeNumpyArray(numpyArray):
    numpyData = {"array": numpyArray}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    return encodedNumpyData

def decodeNumpyArray(encodedNumpyData):
    numpyData = json.loads(encodedNumpyData)
    numpyArray = numpy.asarray(numpyData["array"])
    return numpyArray


if __name__ == "__main__":
    numpyArrayOne = numpy.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    # Serialization
    numpyData = {"array": numpyArrayOne}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file
    print("Printing JSON serialized NumPy array")
    print(encodedNumpyData)

    # Deserialization
    print("Decode JSON serialized NumPy array")
    decodedArrays = json.loads(encodedNumpyData)

    finalNumpyArray = numpy.asarray(decodedArrays["array"])
    print("NumPy Array")
    print(finalNumpyArray)